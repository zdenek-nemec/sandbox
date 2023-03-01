import logging
import timeit

from application_controller import ApplicationController
from application_lock import ApplicationLock
from lucky_numbers import LuckyNumbers

DEFAULT_NUMBER_LIST = [-3, 0, 3, 3.14159, 4 + 2j, 7, "Seven", 13, 21, 42]


def main():
    application_controller = ApplicationController()

    logging.info("Application started")
    application_start_time = timeit.default_timer()
    application_lock = ApplicationLock()

    lucky_numbers = LuckyNumbers(DEFAULT_NUMBER_LIST)
    print("Trending lucky number is " + str(lucky_numbers.get_lucky_number()))

    application_lock.disable()
    application_stop_time = timeit.default_timer()
    logging.debug("Finished in %.1fs" % (application_stop_time - application_start_time))
    logging.info("Application finished")


if __name__ == "__main__":
    main()
