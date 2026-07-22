package com.example.akkademo;

import akka.actor.typed.ActorSystem;
import akka.actor.typed.Behavior;
import akka.actor.typed.SupervisorStrategy;
import akka.actor.typed.javadsl.Behaviors;
import akka.actor.typed.javadsl.Routers;

public class RouterDemo {

    public static void main(String[] args) throws InterruptedException {

        Behavior<Void> guardian = Behaviors.setup(context -> {

            Behavior<WorkerActor.Command> supervised =
                    Behaviors.supervise(WorkerActor.create())
                            .onFailure(RuntimeException.class, SupervisorStrategy.restart());

            // Pool of 3 workers, messages distributed round-robin.
            // The router itself is an actor; callers see a single ActorRef.
            var router = context.spawn(
                    Routers.pool(3, supervised).withRoundRobinRouting(),
                    "worker-pool"
            );

            context.getLog().info("========== ROUTER DEMO (round-robin, 3 workers) ==========");
            context.getLog().info("Sending 6 jobs — each worker should receive exactly 2...");

            for (int i = 1; i <= 6; i++) {
                router.tell(new WorkerActor.DoWork("job-" + i));
            }

            return Behaviors.empty();
        });

        ActorSystem<Void> system = ActorSystem.create(guardian, "router-demo-system");

        // 3 workers process in parallel; each job takes ~500ms, so 2 rounds = ~1s + slack.
        Thread.sleep(4000);
        system.terminate();
    }
}
