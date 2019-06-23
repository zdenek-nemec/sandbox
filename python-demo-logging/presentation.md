# Python Logging Demo

## 1. Hello World
```
print("Hello, World!")
```

## 2. Start logging
```
import logging

logging.basicConfig(filename="my_log.log")
logging.warning("I am about to start")
```

## 3. Log to std-out
```
import sys

logging.basicConfig(stream=sys.stdout)
```

## 4. Log levels
```
logging.debug("This is debug-level message")
logging.info("This is info-level message")
logging.warning("This is warning-level message")
logging.error("This is error-level message")
logging.critical("This is critical-level message")
```

```
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

print(logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR, logging.CRITICAL)
```
