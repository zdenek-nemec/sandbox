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

## 5. Set the log-level with an argument
```
import argparse

parser = argparse.ArgumentParser(prog="Demo")
parser.add_argument("--log_level", "-l", default="WARNING", choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"])

logging.basicConfig(stream=sys.stdout, level=getattr(logging, parser.parse_args().log_level, None))
```

## 6. Set log file with an argument
```
parser.add_argument("--log_file", "-f")

log_file = parser.parse_args().log_file
if log_file is None:
    logging.basicConfig(stream=sys.stdout, level=log_level)
else:
    logging.basicConfig(filename=log_file, level=log_level)
```

## 7. Logging in other modules
```
from demo_module import MyClass

lucky_number = 7
logging.debug("Variable lucky_number is %d" % lucky_number)
my_class = MyClass()
my_class.set_lucky_number(lucky_number)
```

```
class MyClass(object):
    def __init__(self):
        logging.info("Initiating MyClass")
        self._lucky_number = None

    def set_lucky_number(self, number):
        logging.debug("Setting MyClass._lucky_number to %d", number)
        self._lucky_number = number
```

## 8. Format the messages
```
log_format = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(stream=sys.stdout, level=log_level, format=log_format)
```
