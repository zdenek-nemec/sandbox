package com.example.akkademo;

import akka.actor.typed.Behavior;
import akka.actor.typed.PostStop;
import akka.actor.typed.javadsl.AbstractBehavior;
import akka.actor.typed.javadsl.ActorContext;
import akka.actor.typed.javadsl.Behaviors;
import akka.actor.typed.javadsl.Receive;

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
        public DoWork(String job) {
            this.job = job;
        }
    }

    /** Ask the worker to fail on purpose, to demonstrate supervision. */
    public static final class Crash implements Command {}

    // ---- Factory --------------------------------------------------------
    public static Behavior<Command> create() {
        return Behaviors.setup(WorkerActor::new);
    }

    private WorkerActor(ActorContext<Command> context) {
        super(context);
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
        getContext().getLog().info("[{}] Processing '{}' ...", getContext().getSelf().path().name(), msg.job);
        try {
            // Simulates work taking some time. Because the mailbox is sequential,
            // other DoWork messages queued behind this one simply wait their turn.
            Thread.sleep(500);
        } catch (InterruptedException ignored) {
            Thread.currentThread().interrupt();
        }
        getContext().getLog().info("Finished '{}'", msg.job);
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
