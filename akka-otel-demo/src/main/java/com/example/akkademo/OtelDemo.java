package com.example.akkademo;

import akka.actor.typed.ActorSystem;
import akka.actor.typed.Behavior;
import akka.actor.typed.SupervisorStrategy;
import akka.actor.typed.javadsl.Behaviors;
import akka.actor.typed.javadsl.Routers;
import io.opentelemetry.api.trace.Span;
import io.opentelemetry.api.trace.Tracer;
import io.opentelemetry.context.Context;
import io.opentelemetry.context.Scope;
import io.opentelemetry.sdk.OpenTelemetrySdk;
import io.opentelemetry.sdk.trace.SdkTracerProvider;
import io.opentelemetry.sdk.trace.export.SimpleSpanProcessor;

public class OtelDemo {

    public static void main(String[] args) throws InterruptedException {

        // ---- OpenTelemetry setup ----------------------------------------
        SdkTracerProvider tracerProvider = SdkTracerProvider.builder()
                .addSpanProcessor(SimpleSpanProcessor.create(new Slf4jSpanExporter()))
                .build();

        Tracer tracer = OpenTelemetrySdk.builder()
                .setTracerProvider(tracerProvider)
                .build()
                .getTracer("akka-demo");

        // ---- Actor system --------------------------------------------------
        Behavior<Void> guardian = Behaviors.setup(context -> {

            var supervised = Behaviors.supervise(WorkerActor.create(tracer))
                    .onFailure(RuntimeException.class, SupervisorStrategy.restart());

            // Round-robin pool — same setup as RouterDemo, now fully instrumented.
            var router = context.spawn(
                    Routers.pool(3, supervised).withRoundRobinRouting(),
                    "worker-pool"
            );

            context.getLog().info("========== OTEL TRACING DEMO (3 workers, round-robin) ==========");
            context.getLog().info("Each dispatch-job span is the PARENT; worker.process spans are CHILDREN.");
            context.getLog().info("Match spans by traceId to see the parent-child relationship.");

            // Each job gets its own parent span. We capture Context.current() while
            // the span is active and embed it in the message so the worker can link
            // its child span back to this parent — crossing the async actor boundary.
            for (int i = 1; i <= 6; i++) {
                Span parent = tracer.spanBuilder("dispatch-job-" + i).startSpan();
                try (Scope ignored = parent.makeCurrent()) {
                    router.tell(new WorkerActor.DoWork("job-" + i, Context.current()));
                } finally {
                    parent.end();
                }
            }

            return Behaviors.empty();
        });

        ActorSystem<Void> system = ActorSystem.create(guardian, "otel-demo-system");

        // 3 workers in parallel, 2 rounds of ~500ms each = ~1s; extra slack for startup.
        Thread.sleep(4000);
        system.terminate();
        tracerProvider.shutdown();
    }
}
