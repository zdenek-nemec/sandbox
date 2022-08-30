import logging
import os
import socket

from archive_target import ArchiveTarget

ARCHIVE_PATHS = {
    "avl4658t": {
        ArchiveTarget.LIVE: {
            ArchiveTarget.MEDIATION: "/appl/dcs/data01/tmp/OC-12871/mediation_archive",
            ArchiveTarget.TAR: "/appl/dcs/data01/tmp/OC-12871/tar_archive",
            ArchiveTarget.NAS: "/appl/dcs/data01/tmp/OC-12871/nas_archive",
            ArchiveTarget.OPS: "/appl/dcs/data01/tmp/OC-12871/ops_archive"
        },
        ArchiveTarget.TEST: {
            ArchiveTarget.MEDIATION: "/appl/dcs/data01/tmp/OC-12871/tests/target1_mediation",
            ArchiveTarget.TAR: "/appl/dcs/data01/tmp/OC-12871/tests/target2_tar",
            ArchiveTarget.NAS: "/appl/dcs/data01/tmp/OC-12871/tests/target3_nas",
            ArchiveTarget.OPS: "/appl/dcs/data01/tmp/OC-12871/tests/target4_ops"
        }
    },
    "JISKRA": {
        ArchiveTarget.LIVE: {
            ArchiveTarget.MEDIATION: "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/target1_mediation",
            ArchiveTarget.TAR: "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/target2_tar",
            ArchiveTarget.NAS: "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/target3_nas",
            ArchiveTarget.OPS: "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/target4_ops"
        },
        ArchiveTarget.TEST: {
            ArchiveTarget.MEDIATION: "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/target1_mediation",
            ArchiveTarget.TAR: "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/target2_tar",
            ArchiveTarget.NAS: "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/target3_nas",
            ArchiveTarget.OPS: "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/target4_ops"
        }
    },
    "N007510": {
        ArchiveTarget.LIVE: {
            ArchiveTarget.MEDIATION: "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/target1_mediation",
            ArchiveTarget.TAR: "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/target2_tar",
            ArchiveTarget.NAS: "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/target3_nas",
            ArchiveTarget.OPS: "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/target4_ops"
        },
        ArchiveTarget.TEST: {
            ArchiveTarget.MEDIATION: "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/target1_mediation",
            ArchiveTarget.TAR: "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/target2_tar",
            ArchiveTarget.NAS: "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/target3_nas",
            ArchiveTarget.OPS: "C:/Zdenek/Git/GitHub/sandbox/intermediate-tools/archiving/tests/target4_ops"
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
