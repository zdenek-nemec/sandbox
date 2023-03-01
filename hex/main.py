import logging
import timeit

from application_controller import ApplicationController


class Number(object):
    def __init__(self, value: str, base: int = 10):
        self._value = int(value)

    def get_value(self, base: int = 10):
        match base:
            case 2:
                return f"{self._value:b}"
            case 10:
                return f"{self._value}"
            case 16:
                return f"{self._value:x}".upper()
            case _:
                raise ValueError(f"Base {base} is not supported")


def main():
    application_controller = ApplicationController()

    logging.info("Application started")
    application_start_time = timeit.default_timer()

    application_controller.debug_arguments()

    print(f"{Number('10').get_value()=}")
    print(f"{Number('10').get_value(10)=}")
    print(f"{Number('10').get_value(2)=}")
    print(f"{Number('10').get_value(16)=}")
    # print(Number("10").get_value(17))

    application_stop_time = timeit.default_timer()
    logging.debug(f"Finished in {application_stop_time - application_start_time:.1f}s")
    logging.info("Application finished")


if __name__ == "__main__":
    main()
