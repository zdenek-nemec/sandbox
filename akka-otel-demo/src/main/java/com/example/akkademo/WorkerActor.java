package com.example.akkademo;

import akka.actor.typed.Behavior;
import akka.actor.typed.PostStop;
import akka.actor.typed.javadsl.AbstractBehavior;
import akka.actor.typed.javadsl.ActorContext;
import akka.actor.typed.javadsl.Behaviors;
import akka.actor.typed.javadsl.Receive;
import io.opentelemetry.api.OpenTelemetry;
import io.opentelemetry.api.trace.Span;
import io.opentelemetry.api.trace.Tracer;
import io.opentelemetry.context.Context;
import io.opentelemetry.context.Scope;

/**
 * A minimal actor to demonstrate three core Akka concepts:
 *
 * 1. PROTOCOL: an actor only understands a fixed set of message types (its "Command"s).
 *              You never call methods on it directly, you send it messages.
 * 2. MAILBOX:  messages sent to this actor are queued and handled ONE AT A TIME, in order,
 *              even if they arrive concurrently from multiple senders.
 * 3. LIFECYCLE: when supervision restarts this actor after a crash, a brand-new instance
 *              is created (constructor runs again) but the ActorRef the outside world
 *              holds does not change.
 */
public class WorkerActor extends AbstractBehavior<WorkerActor.Command> {

    // ---- Protocol -----------------------------------------------------
    // Sealed-ish interface: every message this actor accepts implements Command.
    public interface Command {}

    /** Ask the worker to do some (simulated) work. */
    public static final class DoWork implements Command {
        public final String job;
        public final Context context;

        public DoWork(String job) {
            this(job, Context.current());
        }

        // Explicit context overload used when the caller holds an active span
        // and wants the worker's span to appear as a child in the trace.
        public DoWork(String job, Context context) {
            this.job = job;
            this.context = context;
        }
    }

    /** Ask the worker to fail on purpose, to demonstrate supervision. */
    public static final class Crash implements Command {}

    // ---- Factory --------------------------------------------------------
    public static Behavior<Command> create() {
        return create(OpenTelemetry.noop().getTracer("noop"));
    }

    public static Behavior<Command> create(Tracer tracer) {
        return Behaviors.setup(ctx -> new WorkerActor(ctx, tracer));
    }

    private final Tracer tracer;

    private WorkerActor(ActorContext<Command> context, Tracer tracer) {
        super(context);
        this.tracer = tracer;
        getContext().getLog().info(">>> Worker instance CREATED");
    }

    // ---- Message handling -------------------------------------------------
    @Override
    public Receive<Command> createReceive() {
        return newReceiveBuilder()
                .onMessage(DoWork.class, this::onDoWork)
                .onMessage(Crash.class, this::onCrash)
                .onSignal(PostStop.class, signal -> onPostStop())
                .build();
    }

    private Behavior<Command> onDoWork(DoWork msg) {
        Span span = tracer.spanBuilder("worker.process")
                .setParent(msg.context)
                .setAttribute("job", msg.job)
                .setAttribute("worker", getContext().getSelf().path().name())
                .startSpan();
        try (Scope ignored = span.makeCurrent()) {
            getContext().getLog().info("[{}] Processing '{}' ...", getContext().getSelf().path().name(), msg.job);
            // Simulates work taking some time. Because the mailbox is sequential,
            // other DoWork messages queued behind this one simply wait their turn.
            try {
                Thread.sleep(500);
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
            getContext().getLog().info("Finished '{}'", msg.job);
        } finally {
            span.end();
        }
        return this;
    }

    private Behavior<Command> onCrash(Crash msg) {
        getContext().getLog().info("About to throw an exception on purpose...");
        throw new RuntimeException("Simulated failure while handling a message");
    }

    private Behavior<Command> onPostStop() {
        getContext().getLog().info("<<< Worker instance STOPPED");
        return this;
    }
}
