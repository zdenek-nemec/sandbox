from enum import Enum


class ArchiveTarget(Enum):
    ENVIRONMENT_LOCAL = 1
    ENVIRONMENT_TEST = 2
    ENVIRONMENT_PRODUCTION = 3
    PATH_MEDIATION = 1
    PATH_TEMPORARY = 2
    PATH_LOGS = 3
    PATH_ORIGINALS = 4
    PATH_TAR = 5


if __name__ == "__main__":
    pass
