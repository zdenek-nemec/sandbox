import socket

DEFAULT_LOCK_PORT = 12345


class ApplicationLock(object):
    def __init__(self, port=DEFAULT_LOCK_PORT):
        self._socket = socket.socket()
        self._port = port
        self._lock()

    def _lock(self):
        try:
            self._socket.bind((socket.gethostname(), self._port))
        except OSError:
            self._socket.close()
            raise RuntimeError("The application is running already, cannot start another instance")

    def disable(self):
        self._socket.close()


if __name__ == "__main__":
    pass
