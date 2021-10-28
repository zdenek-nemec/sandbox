import multiprocessing
import time


def loop_forever(a, b, c):
    while True:
        print("Waiting... %d %s %d" % (a, b, c))
        a += 1
        # if a >= 4:
        #     return
        time.sleep(1)


def main():
    """Python timeout demonstration with Multiprocessing module."""
    print("Hello, World!")
    process = multiprocessing.Process(target=loop_forever, args=(1, "2222", 3))
    process.start()
    process.join(10)
    if process.is_alive():
        print("It is still alive, let's kill it!")
        process.terminate()
        process.join()
    print("Finished")

if __name__ == "__main__":
    main()
