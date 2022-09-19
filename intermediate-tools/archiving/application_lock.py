import logging
import socket

DEFAULT_LOCK_PORT = 12345


class ApplicationLock(object):
    def __init__(self, port=DEFAULT_LOCK_PORT):
        self._socket = socket.socket()
        self._port = port
        self._lock()

    def _lock(self):
        logging.debug("Attempting to lock a single application instance via port {0}".format(self._port))
        try:
            self._socket.bind((socket.gethostname(), self._port))
        except OSError:
            logging.error("The application is running already, cannot start another instance")
            self._socket.close()
            raise
        else:
            logging.debug("This is the only running application instance, the process continues")

    def disable(self):
        self._socket.close()


if __name__ == "__main__":
    pass
