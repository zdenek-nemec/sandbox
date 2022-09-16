import logging
import os
import socket

from archive_target import ArchiveTarget

ARCHIVE_PATHS = {
    "avl4688t": {  # Intermediate 9 Development
        ArchiveTarget.LIVE_ENV: {
            ArchiveTarget.MED_PATH: "/appl/dcs/data01/ARCHIVE",
            ArchiveTarget.TAR_PATH: "/appl/dcs/data01/ARCHIVE/ARCHIVE_STORAGE/temp",
            ArchiveTarget.LOG_PATH: "/appl/dcs/data01/ARCHIVE/ARCHIVE_STORAGE/logs",
            ArchiveTarget.OPS_PATH: "/appl/dcs/data01/ARCHIVE/ARCHIVE_STORAGE/originals",
            ArchiveTarget.NAS_PATH: "/appl/dcs/data01/ARCHIVE/ARCHIVE_STORAGE/tar"
        },
        ArchiveTarget.TEST_ENV: {
            ArchiveTarget.MED_PATH: "/appl/dcs/data01/SOFTWARE/Tools/Archiving/tests/mediation",
            ArchiveTarget.TAR_PATH: "/appl/dcs/data01/SOFTWARE/Tools/Archiving/tests/temp",
            ArchiveTarget.LOG_PATH: "/appl/dcs/data01/SOFTWARE/Tools/Archiving/tests/logs",
            ArchiveTarget.OPS_PATH: "/appl/dcs/data01/SOFTWARE/Tools/Archiving/tests/originals",
            ArchiveTarget.NAS_PATH: "/appl/dcs/data01/SOFTWARE/Tools/Archiving/tests/tar"
        }
    },
    "avl4658t": {  # Intermediate 9 Test
        ArchiveTarget.LIVE_ENV: {
            ArchiveTarget.MED_PATH: "/appl/dcs/data01/ARCHIVE",
            ArchiveTarget.TAR_PATH: "/appl/dcs/data01/ARCHIVE/ARCHIVE_STORAGE/temp",
            ArchiveTarget.LOG_PATH: "/appl/dcs/data01/ARCHIVE/ARCHIVE_STORAGE/logs",
            ArchiveTarget.OPS_PATH: "/appl/dcs/data01/ARCHIVE/ARCHIVE_STORAGE/originals",
            ArchiveTarget.NAS_PATH: "/appl/dcs/data01/ARCHIVE/ARCHIVE_STORAGE/tar"
        },
        ArchiveTarget.TEST_ENV: {
            ArchiveTarget.MED_PATH: "/appl/dcs/data01/SOFTWARE/Tools/Archiving/tests/mediation",
            ArchiveTarget.TAR_PATH: "/appl/dcs/data01/SOFTWARE/Tools/Archiving/tests/temp",
            ArchiveTarget.LOG_PATH: "/appl/dcs/data01/SOFTWARE/Tools/Archiving/tests/logs",
            ArchiveTarget.OPS_PATH: "/appl/dcs/data01/SOFTWARE/Tools/Archiving/tests/originals",
            ArchiveTarget.NAS_PATH: "/appl/dcs/data01/SOFTWARE/Tools/Archiving/tests/tar"
        }
    },
    "JISKRA": {  # Zdenek
        ArchiveTarget.LIVE_ENV: {
            ArchiveTarget.MED_PATH: "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/mediation",
            ArchiveTarget.TAR_PATH: "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/temp",
            ArchiveTarget.LOG_PATH: "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/logs",
            ArchiveTarget.OPS_PATH: "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/originals",
            ArchiveTarget.NAS_PATH: "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/tar"
        },
        ArchiveTarget.TEST_ENV: {
            ArchiveTarget.MED_PATH: "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/mediation",
            ArchiveTarget.TAR_PATH: "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/temp",
            ArchiveTarget.LOG_PATH: "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/logs",
            ArchiveTarget.OPS_PATH: "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/originals",
            ArchiveTarget.NAS_PATH: "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/tar"
        }
    },
    "N007510": {  # Zdenek
        ArchiveTarget.LIVE_ENV: {
            ArchiveTarget.MED_PATH: "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/mediation",
            ArchiveTarget.TAR_PATH: "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/temp",
            ArchiveTarget.LOG_PATH: "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/logs",
            ArchiveTarget.OPS_PATH: "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/originals",
            ArchiveTarget.NAS_PATH: "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/tar"
        },
        ArchiveTarget.TEST_ENV: {
            ArchiveTarget.MED_PATH: "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/mediation",
            ArchiveTarget.TAR_PATH: "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/temp",
            ArchiveTarget.LOG_PATH: "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/logs",
            ArchiveTarget.OPS_PATH: "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/originals",
            ArchiveTarget.NAS_PATH: "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/tar"
        }
    }
}


class ArchivePaths(object):
    def __init__(self, is_live: bool = False):
        self._is_live = is_live
        self._host = socket.gethostname()
        self._valid_hosts = list(ARCHIVE_PATHS.keys())

    def is_live(self):
        return self._is_live

    def is_host_valid(self):
        return self._host in self._valid_hosts

    def get_host(self):
        return self._host

    def get_path(self, target: ArchiveTarget):
        environment = ArchiveTarget.LIVE_ENV if self._is_live else ArchiveTarget.TEST_ENV
        try:
            return os.path.normpath(ARCHIVE_PATHS[self._host][environment][target])
        except KeyError:
            logging.error(
                "Unexpected archive target requested: host {0}, environment {1}, target {2}".format(
                    self._host, environment, target
                )
            )
            raise


if __name__ == "__main__":
    pass
