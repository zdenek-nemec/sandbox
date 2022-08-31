import logging
import os
import socket

from archive_target import ArchiveTarget

ARCHIVE_PATHS = {
    "avl4658t": {
        ArchiveTarget.LIVE: {
            ArchiveTarget.MED: "/appl/dcs/data01/tmp/OC-12871/med_archive",
            ArchiveTarget.TAR: "/appl/dcs/data01/tmp/OC-12871/tar_archive",
            ArchiveTarget.NAS: "/appl/dcs/data01/tmp/OC-12871/nas_archive",
            ArchiveTarget.OPS: "/appl/dcs/data01/tmp/OC-12871/ops_archive"
        },
        ArchiveTarget.TEST: {
            ArchiveTarget.MED: "/appl/dcs/data01/tmp/OC-12871/tests/med_archive",
            ArchiveTarget.TAR: "/appl/dcs/data01/tmp/OC-12871/tests/tar_archive",
            ArchiveTarget.NAS: "/appl/dcs/data01/tmp/OC-12871/tests/nas_archive",
            ArchiveTarget.OPS: "/appl/dcs/data01/tmp/OC-12871/tests/ops_archive"
        }
    },
    "JISKRA": {
        ArchiveTarget.LIVE: {
            ArchiveTarget.MED: "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/med_archive",
            ArchiveTarget.TAR: "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/tar_archive",
            ArchiveTarget.NAS: "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/nas_archive",
            ArchiveTarget.OPS: "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/ops_archive"
        },
        ArchiveTarget.TEST: {
            ArchiveTarget.MED: "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/med_archive",
            ArchiveTarget.TAR: "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/tar_archive",
            ArchiveTarget.NAS: "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/nas_archive",
            ArchiveTarget.OPS: "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/ops_archive"
        }
    },
    "N007510": {
        ArchiveTarget.LIVE: {
            ArchiveTarget.MED: "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/med_archive",
            ArchiveTarget.TAR: "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/tar_archive",
            ArchiveTarget.NAS: "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/nas_archive",
            ArchiveTarget.OPS: "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/ops_archive"
        },
        ArchiveTarget.TEST: {
            ArchiveTarget.MED: "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/med_archive",
            ArchiveTarget.TAR: "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/tar_archive",
            ArchiveTarget.NAS: "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/nas_archive",
            ArchiveTarget.OPS: "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/ops_archive"
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
        environment = ArchiveTarget.LIVE if self._is_live else ArchiveTarget.TEST
        try:
            return os.path.normpath(ARCHIVE_PATHS[self._host][environment][target])
        except KeyError:
            logging.error(
                "Unexpected target path requested: host {0}, environment {1}, target {2}".format(
                    self._host, environment, target
                )
            )
            raise


if __name__ == "__main__":
    pass
