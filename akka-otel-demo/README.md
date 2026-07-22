# Akka and OTEL

Akka Actor Model Demo (Java) by Claude

A minimal Maven project demonstrating three core Akka concepts:

1. **Mailbox** – messages sent to an actor are queued and processed strictly one at a time, in order.
2. **Supervision** – when an actor throws an exception, its parent's supervision strategy decides what happens (here: `restart`).
3. **Lifecycle** – on restart, a brand-new actor instance is created, but the `ActorRef` the rest of the system holds stays valid and keeps working transparently.

## Requirements

- JDK 21 (check with `java -version` in a terminal) — matched to the production app's Java version
- IntelliJ IDEA (Community or Ultimate)
- Internet access the first time you open the project, so Maven can download Akka + logback from Maven Central

**Note on the Akka version**: this project pins `akka.version` to `2.6.20`, the last Akka release published to plain Maven Central under the Apache 2.0 license. Akka 2.7+ (including the current 2.10.x line) moved to a Business Source License and is only distributed via Lightbend's own tokenized repository (a free account at `account.akka.io` gets you a token, but it's an extra setup step). The actor API used in this demo (`AbstractBehavior`, `Behaviors.supervise`, etc.) is identical between 2.6.x and the current release, so this doesn't change anything you're learning here. If your production Scala app uses a newer Akka version and you want the demo to match exactly, let me know and I'll wire up the tokenized repository instead.

## Setup in IntelliJ (Linux Mint)

1. Unzip this project somewhere, e.g. `~/projects/akka-demo`.
2. In IntelliJ: **File → Open...** and select the `akka-demo` folder (the one containing `pom.xml`).
3. IntelliJ will detect it's a Maven project and prompt to import it — click **Load Maven Project** / **Trust Project** if asked.
4. Wait for the Maven sync to finish (progress bar bottom-right). It will download the Akka and Logback jars.
5. Open `src/main/java/com/example/akkademo/Main.java`.
6. Click the green ▶ run arrow next to `public static void main` (or right-click the file → **Run 'Main.main()'**).

If IntelliJ complains about the project SDK, go to **File → Project Structure → Project** and set the SDK to a JDK 17 (or newer) install.

## What to watch for in the console output

Run it and read the log timestamps top to bottom:

- **Mailbox demo**: `job-1`, `job-2`, `job-3` are all `tell()`-ed instantly with no delay between the calls, but the logs show them starting ~500ms apart — proof they're handled sequentially by the same actor, not in parallel.
- **Supervision demo**: after the `Crash` message, you'll see:
  - `About to throw an exception on purpose...`
  - `<<< Worker instance STOPPED` (the crashed instance being torn down)
  - `>>> Worker instance CREATED` (a fresh instance replacing it)
  - then `job-4` and `job-5` still get processed normally, sent to the *exact same* `worker` variable/`ActorRef` as before the crash.

## Things to try next (optional, to build intuition)

- Change `SupervisorStrategy.restart()` to `SupervisorStrategy.stop()` and see that `job-4`/`job-5` are now silently dropped (the actor is gone, but the `ActorRef` still accepts `tell()` calls without erroring — this is a common source of confusion when debugging real systems).
- Change `SupervisorStrategy.restart()` to `SupervisorStrategy.resume()` and see the difference: no STOPPED/CREATED lifecycle logs at all, the actor just carries on with the next message as if nothing happened.
- Send 20 `DoWork` messages instead of 3 and watch them queue up — this is exactly the kind of mailbox backpressure that's worth knowing about when debugging a slow or stuck Akka actor in production.

## Next step

Once you're comfortable with this, we'll extend the same project with OpenTelemetry: adding spans around `DoWork` handling and propagating trace context from `Main` into the actor, so a single logical request is traceable across the async boundary.
