# Intermediate Tools: Archiving

Main

* `archive.sh`
* `archive.py`
* `README.md`

Secondary

* `.gitignore`
* `application_lock.py`
* `archive_paths.py`
* `archive_target.py`
* `gimme_files.py`
* `prepare_test_data.py`
* `test_application_lock.py`
* `test_archive_paths.py`

Implemented in Bash and Python 3.8

Dependencies

* `parameterized`

Synopsis

```text
archive.sh

archive.py [--live]
```

Examples

```text
archive.sh

archive.py
archive.py --live
```

Installation on Intermediate 9 server

```text
# TAR Archiving
15 * * * * /appl/dcs/data01/SOFTWARE/Tools/Archiving/archive.sh
```

## To Do

* [x] Exclusions
* [x] Refactor `archive_paths.py`
* [x] Monthly directories in TAR target
* [x] Monthly directories in `logs`
* [ ] Create `tar.tmp` first and then change to `.tar`
* [x] Check paths: archive `temp`, `archive_logs`, `originals`, `tar_archives` and application logs
* [ ] Option to preserve or delete originals
* [ ] Select date (and time) for TAR creation
* [x] Handle valid files in arch01 - TAR filename starts with dash `-`
* [x] Handle weird filenames (with spaces)
* [x] Make sure the application cannot run more than once at a time
* [ ] Common functions (e.g. `validate_path`)
* [ ] Go directory after directory instead of creating complete list at the start

### Extra

* [ ] Provide restore application
* [ ] Provide statistics script for OPS
  * [ ] How many files were collected by `ICS|*_SSS` between 02:00 and 03:00

### Maybe

* [ ] Logs directory structure mirrors TAR
