import time
import timeit


def main():
    start_time = timeit.default_timer()
    print("TimeIt Module Demo - Start")
    time.sleep(2)
    print("TimeIt Module Demo - End")
    stop_time = timeit.default_timer()
    print("[Finished in %.1fs]" % (stop_time - start_time))


if __name__ == "__main__":
    main()
