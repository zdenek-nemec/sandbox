import logging
import os
import socket

from archive_target import ArchiveTarget

ARCHIVE_PATHS = {
    "avl4658t": {
        ArchiveTarget.LIVE_ENV: {
            ArchiveTarget.MED_PATH: "/appl/dcs/data01/tmp/OC-12871/med_archive",
            ArchiveTarget.TAR_PATH: "/appl/dcs/data01/tmp/OC-12871/tar_archive",
            ArchiveTarget.NAS_PATH: "/appl/dcs/data01/tmp/OC-12871/nas_archive",
            ArchiveTarget.OPS_PATH: "/appl/dcs/data01/tmp/OC-12871/ops_archive",
            ArchiveTarget.LOG_PATH: "/appl/dcs/data01/tmp/OC-12871/log_archive"
        },
        ArchiveTarget.TEST_ENV: {
            ArchiveTarget.MED_PATH: "/appl/dcs/data01/tmp/OC-12871/tests/med_archive",
            ArchiveTarget.TAR_PATH: "/appl/dcs/data01/tmp/OC-12871/tests/tar_archive",
            ArchiveTarget.NAS_PATH: "/appl/dcs/data01/tmp/OC-12871/tests/nas_archive",
            ArchiveTarget.OPS_PATH: "/appl/dcs/data01/tmp/OC-12871/tests/ops_archive",
            ArchiveTarget.LOG_PATH: "/appl/dcs/data01/tmp/OC-12871/tests/log_archive"
        }
    },
    "JISKRA": {
        ArchiveTarget.LIVE_ENV: {
            ArchiveTarget.MED_PATH: "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/med_archive",
            ArchiveTarget.TAR_PATH: "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/tar_archive",
            ArchiveTarget.NAS_PATH: "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/nas_archive",
            ArchiveTarget.OPS_PATH: "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/ops_archive",
            ArchiveTarget.LOG_PATH: "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/log_archive"
        },
        ArchiveTarget.TEST_ENV: {
            ArchiveTarget.MED_PATH: "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/med_archive",
            ArchiveTarget.TAR_PATH: "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/tar_archive",
            ArchiveTarget.NAS_PATH: "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/nas_archive",
            ArchiveTarget.OPS_PATH: "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/ops_archive",
            ArchiveTarget.LOG_PATH: "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/log_archive"
        }
    },
    "N007510": {
        ArchiveTarget.LIVE_ENV: {
            ArchiveTarget.MED_PATH: "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/med_archive",
            ArchiveTarget.TAR_PATH: "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/tar_archive",
            ArchiveTarget.NAS_PATH: "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/nas_archive",
            ArchiveTarget.OPS_PATH: "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/ops_archive",
            ArchiveTarget.LOG_PATH: "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/log_archive"
        },
        ArchiveTarget.TEST_ENV: {
            ArchiveTarget.MED_PATH: "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/med_archive",
            ArchiveTarget.TAR_PATH: "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/tar_archive",
            ArchiveTarget.NAS_PATH: "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/nas_archive",
            ArchiveTarget.OPS_PATH: "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/ops_archive",
            ArchiveTarget.LOG_PATH: "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/log_archive"
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
