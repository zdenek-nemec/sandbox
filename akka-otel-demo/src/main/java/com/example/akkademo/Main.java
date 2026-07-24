package com.example.akkademo;

import akka.actor.typed.ActorRef;
import akka.actor.typed.ActorSystem;
import akka.actor.typed.Behavior;
import akka.actor.typed.SupervisorStrategy;
import akka.actor.typed.javadsl.AskPattern;
import akka.actor.typed.javadsl.Behaviors;

import java.time.Duration;
import java.util.concurrent.CompletionStage;

public class Main {

    public static void main(String[] args) throws InterruptedException {

        // The "guardian" behavior: the root actor of the whole system.
        // Its only job here is to spawn the worker and kick off the demo.
        Behavior<Void> guardian = Behaviors.setup(context -> {

            // Wrap WorkerActor's behavior with a supervision strategy.
            // "restart" means: on any RuntimeException, throw away the failed
            // instance and create a fresh one automatically. The ActorRef
            // returned by spawn() stays valid the whole time.
            Behavior<WorkerActor.Command> supervised =
                    Behaviors.supervise(WorkerActor.create())
                            .onFailure(RuntimeException.class, SupervisorStrategy.restart());

//            var worker1 = context.spawn(supervised, "worker-1");
//            var worker2 = context.spawn(supervised, "worker-2");
//
//            context.getLog().info("========== MAILBOX DEMO ==========");
//            context.getLog().info("Sending 3 messages back-to-back (no waiting)...");
//            // These three are enqueued instantly. Watch the logs: they are still
//            // processed strictly one-at-a-time, ~500ms apart, in the order sent.
//            worker1.tell(new WorkerActor.DoWork("job-1"));
//            worker2.tell(new WorkerActor.DoWork("job-2"));
//            worker1.tell(new WorkerActor.DoWork("job-3"));
//
//            context.getLog().info("========== SUPERVISION DEMO ==========");
//            context.getLog().info("Sending a message that makes the actor crash...");
//            // This message throws inside the actor. Because of the "restart" strategy:
//            //  - the actor logs "STOPPED" for the crashed instance
//            //  - a new instance is created (you'll see "CREATED" again)
//            //  - the queued messages behind it (job-4, job-5) still get processed
//            worker1.tell(new WorkerActor.Crash());
//
//            context.getLog().info("Sending 2 more messages to the SAME ActorRef...");
//            worker1.tell(new WorkerActor.DoWork("job-4"));
//            worker2.tell(new WorkerActor.DoWork("job-5"));

            context.getLog().info("========== PARAMETERIZED MESSAGE DEMO ==========");
            var calculator = context.spawn(CalculatorActor.create(), "calculator");
            Duration askTimeout = Duration.ofSeconds(3);

            // "ask" sends a message carrying parameters (3, 4) AND a reply address,
            // and gives us back a CompletionStage we can react to once the actor answers.
            CompletionStage<CalculatorActor.Result> sum =
                    AskPattern.ask(
                            calculator,
                            (ActorRef<CalculatorActor.Result> replyTo) ->
                                    new CalculatorActor.Add(3, 4, replyTo),
                            askTimeout,
                            context.getSystem().scheduler());

            sum.whenComplete((result, failure) -> {
                if (failure != null) {
                    context.getLog().error("Add request failed or timed out", failure);
                } else {
                    context.getLog().info("Got reply: 3 + 4 = {}", result.value);
                }
            });

            CompletionStage<CalculatorActor.Result> product =
                    AskPattern.ask(
                            calculator,
                            (ActorRef<CalculatorActor.Result> replyTo) ->
                                    new CalculatorActor.Multiply(3, 4, replyTo),
                            askTimeout,
                            context.getSystem().scheduler());

            product.whenComplete((result, failure) -> {
                if (failure != null) {
                    context.getLog().error("Multiply request failed or timed out", failure);
                } else {
                    context.getLog().info("Got reply: 3 * 4 = {}", result.value);
                }
            });

            return Behaviors.empty();
        });

        ActorSystem<Void> system = ActorSystem.create(guardian, "akka-demo-system");

        // Give the actor system enough time to process everything before we exit.
        Thread.sleep(6000);
        system.terminate();
    }
}
