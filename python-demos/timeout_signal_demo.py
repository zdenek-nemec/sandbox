import signal
import time


def handler(signum, frame):
    print("Forever is over!")
    raise Exception("Exception: End of waiting.")


def loop_forever():
    while True:
        print("Waiting...")
        time.sleep(1)


def main():
    """Python timeout demonstration with Signal module.
       Works on Unix only!
    """
    print("Hello, World!")
    signal.signal(signal.SIGALRM, handler)
    signal.alarm(10)
    try:
        loop_forever()
    except Exception as exc:
        print(exc)
    signal.alarm(0)


if __name__ == "__main__":
    main()
