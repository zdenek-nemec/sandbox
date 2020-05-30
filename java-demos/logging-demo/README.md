# Java Logging Demo

Sources:

* [Vogella Java Logging API Tutorial](https://www.vogella.com/tutorials/Logging/article.html)
* [Java Code Geeks Example](https://examples.javacodegeeks.com/core-java/util/logging/java-util-logging-example/)
* [Java Class Level](https://docs.oracle.com/javase/7/docs/api/java/util/logging/Level.html)

Log Levels:

| Level   | Value               | Description                      |
| ------- | ------------------- | -------------------------------- |
| OFF     | `Integer.MAX_VALUE` | Logging off.                     |
| SEVERE  | 1000                | Exceptions and program failures. | 
| WARNING | 900                 | Recoverable failures.            |
| INFO    | 800                 | Significant events.              | 
| CONFIG  | 700                 | Configuration details.           |
| FINE    | 500                 | Program events.                  |
| FINER   | 400                 | Entering and exiting methods.    |
| FINEST  | 300                 | Loop iterations.                 | 
| ALL     | `Integer.MIN_VALUE` | Log everything.                  |

Best Practises

* Do not use global logger, create separate logger per class. This will allow
  handling these loggers separately.
