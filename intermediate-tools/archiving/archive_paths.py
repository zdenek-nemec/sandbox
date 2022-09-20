import logging
import os
import socket

from archive_target import ArchiveTarget

INTERMEDIATE = {
    "avl4688t": ArchiveTarget.ENVIRONMENT_TEST,
    "avl4658t": ArchiveTarget.ENVIRONMENT_TEST,
    "avl4713p": ArchiveTarget.ENVIRONMENT_PRODUCTION,
    "avl4715p": ArchiveTarget.ENVIRONMENT_PRODUCTION
}

ARCHIVE_PATHS = {
    ArchiveTarget.ENVIRONMENT_LOCAL: {
        ArchiveTarget.PATH_MEDIATION: "./tests/mediation",
        ArchiveTarget.PATH_TEMPORARY: "./tests/temp",
        ArchiveTarget.PATH_LOGS: "./tests/archive_logs",
        ArchiveTarget.PATH_ORIGINALS: "./tests/originals",
        ArchiveTarget.PATH_TAR: "./tests/tar_archives"
    },
    ArchiveTarget.ENVIRONMENT_TEST: {
        ArchiveTarget.PATH_MEDIATION: "/appl/dcs/data01/ARCHIVE",
        ArchiveTarget.PATH_TEMPORARY: "/appl/dcs/data01/ARCHIVE/ARCHIVE_STORAGE/temp",
        ArchiveTarget.PATH_LOGS: "/appl/dcs/data01/ARCHIVE/ARCHIVE_STORAGE/archive_logs",
        ArchiveTarget.PATH_ORIGINALS: "/appl/dcs/data01/ARCHIVE/ARCHIVE_STORAGE/originals",
        ArchiveTarget.PATH_TAR: "/appl/dcs/data01/ARCHIVE/ARCHIVE_STORAGE/tar_archives"
    },
    ArchiveTarget.ENVIRONMENT_PRODUCTION: {
        ArchiveTarget.PATH_MEDIATION: "/appl/dcs/data01/tmp/OC-12871/arch01",
        ArchiveTarget.PATH_TEMPORARY: "/appl/dcs/data01/tmp/OC-12871/temp",
        ArchiveTarget.PATH_LOGS: "/appl/dcs/data01/tmp/OC-12871/archive_logs",
        ArchiveTarget.PATH_ORIGINALS: "/appl/dcs/data01/tmp/OC-12871/originals",
        ArchiveTarget.PATH_TAR: "/appl/dcs/data01/tmp/OC-12871/tar_archives"
    }
}


class ArchivePaths(object):
    def __init__(self, test: bool = False):
        self._host = socket.gethostname()
        self._test = test or self._host not in INTERMEDIATE.keys()

    def _get_path_value(self, environment, target):
        try:
            return os.path.abspath(ARCHIVE_PATHS[environment][target])
        except KeyError:
            logging.error(
                "Unexpected archive target requested: host {0}, environment {1}, target {2}".format(
                    self._host, environment, target
                )
            )
            raise

    def is_test(self):
        return self._test

    def get_path(self, target: ArchiveTarget):
        environment = ArchiveTarget.ENVIRONMENT_LOCAL if self._test else INTERMEDIATE[self._host]
        return self._get_path_value(environment, target)

    def validate(self, path):
        if not os.path.isdir(path):
            raise OSError("Path {0} does not exist".format(path))


if __name__ == "__main__":
    pass
