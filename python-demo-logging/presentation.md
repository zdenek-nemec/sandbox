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
