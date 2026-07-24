package com.example.akkademo;

import akka.actor.typed.ActorRef;
import akka.actor.typed.Behavior;
import akka.actor.typed.javadsl.AbstractBehavior;
import akka.actor.typed.javadsl.ActorContext;
import akka.actor.typed.javadsl.Behaviors;
import akka.actor.typed.javadsl.Receive;

/**
 * Demonstrates messages that carry MULTIPLE PARAMETERS plus a "replyTo"
 * address, so the sender gets an actual answer back instead of just
 * fire-and-forget. This request/response shape (driven from outside via
 * the "ask pattern") is one of the most common message shapes in real
 * Akka systems — e.g. "look up this customer and tell me the result".
 *
 * Contrast with WorkerActor.DoWork(String job): that carries one parameter
 * and gets no reply. Here, Add/Multiply carry two parameters (a, b) AND
 * a reply channel, so the caller receives a Result back asynchronously.
 */
public class CalculatorActor extends AbstractBehavior<CalculatorActor.Command> {

    // ---- Protocol -----------------------------------------------------
    public interface Command {}

    /** Carries two int parameters plus where to send the answer. */
    public static final class Add implements Command {
        public final int a;
        public final int b;
        public final ActorRef<Result> replyTo;

        public Add(int a, int b, ActorRef<Result> replyTo) {
            this.a = a;
            this.b = b;
            this.replyTo = replyTo;
        }
    }

    public static final class Multiply implements Command {
        public final int a;
        public final int b;
        public final ActorRef<Result> replyTo;

        public Multiply(int a, int b, ActorRef<Result> replyTo) {
            this.a = a;
            this.b = b;
            this.replyTo = replyTo;
        }
    }

    /** The response message, sent back to whoever is listening at replyTo. */
    public static final class Result {
        public final int value;

        public Result(int value) {
            this.value = value;
        }
    }

    // ---- Factory --------------------------------------------------------
    public static Behavior<Command> create() {
        return Behaviors.setup(CalculatorActor::new);
    }

    private CalculatorActor(ActorContext<Command> context) {
        super(context);
    }

    // ---- Message handling -------------------------------------------------
    @Override
    public Receive<Command> createReceive() {
        return newReceiveBuilder()
                .onMessage(Add.class, this::onAdd)
                .onMessage(Multiply.class, this::onMultiply)
                .build();
    }

    private Behavior<Command> onAdd(Add msg) {
        int sum = msg.a + msg.b;
        getContext().getLog().info("Handling Add({}, {}) -> {}", msg.a, msg.b, sum);
        msg.replyTo.tell(new Result(sum));
        return this;
    }

    private Behavior<Command> onMultiply(Multiply msg) {
        int product = msg.a * msg.b;
        getContext().getLog().info("Handling Multiply({}, {}) -> {}", msg.a, msg.b, product);
        msg.replyTo.tell(new Result(product));
        return this;
    }
}
