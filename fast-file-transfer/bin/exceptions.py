#!/usr/bin/env python3


class Error(Exception):
    """Basic exception for errors raised by Fast File Transfer application"""
    pass


class CannotBuildDataConnectionError(Error):
    """Cannot build data connection"""
    def __init__(self, message=None):
        if message is None:
            message = "Cannot build data connection"
        super(CannotBuildDataConnectionError, self).__init__(message)


class CorruptedFileError(Error):
    """Collected file is corrupted"""
    def __init__(self, message=None):
        if message is None:
            message = "Collected file is corrupted"
        super(CorruptedFile, self).__init__(message)


class SourceFileNotFoundError(Error):
    """Source file does not exist"""
    def __init__(self, message=None):
        if message is None:
            message = "Source file does not exist"
        super(SourceFileNotFoundError, self).__init__(message)


if __name__ == "__main__":
    pass
