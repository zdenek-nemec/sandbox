import multiprocessing
import time


def loop_forever():
    while True:
        print("Waiting...")
        time.sleep(1)


def main():
    """Python timeout demonstration with Multiprocessing module."""
    print("Hello, World!")
    process = multiprocessing.Process(target=loop_forever)
    process.start()
    process.join(10)
    if process.is_alive():
        print("It is still alive, let's kill it!")
        process.terminate()
        process.join()


if __name__ == "__main__":
    main()
