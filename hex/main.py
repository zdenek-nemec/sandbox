import logging
import timeit

from application_controller import ApplicationController


def main():
    application_controller = ApplicationController()

    logging.info("Application started")
    application_start_time = timeit.default_timer()

    application_stop_time = timeit.default_timer()
    logging.debug("Finished in %.1fs" % (application_stop_time - application_start_time))
    logging.info("Application finished")


if __name__ == "__main__":
    main()
