# Intermediate Tools: Archiving

Implemented in Bash and Python 3.

* Python 3.7.8
* Python 3.8.2

## Structure

Main

* `archive.sh` - Script for running the archive application on Intermediate servers
* `archive.py` - Python application for archiving Intermediate input files
* `README.md` - Documentation

Secondary

* `.gitignore`
* `application_lock.py`
* `archive_paths.py`
* `archive_target.py`
* `gimme_files.py` - Application for retrieving files from TAR archives, in progress
* `prepare_test_data.py` - Script for setting up system test locally
* `test_application_lock.py` - Unit tests
* `test_archive_paths.py` - Unit tests

## Dependencies

* `parameterized` - Only for unit tests

## Synopsis

```text
archive.sh
```

```text
archive.py [--help] [--log_level {DEBUG,INFO,WARNING,ERROR,CRITICAL}] [--live] [--date DATE] [--originals {MOVE,DELETE}]
```

## Installation

1. Copy all files to the server, ideally to `/appl/dcs/data01/SOFTWARE/Tools/Archiving`
2. Assign 744 permissions to `archive.sh`
3. Run manually or set up following Cron job
   
    ```text
    # TAR Archiving
    15 * * * * /appl/dcs/data01/SOFTWARE/Tools/Archiving/archive.sh
    ```

## To Do

* [x] Exclusions
* [x] Monthly directories in TAR target
* [x] Monthly directories in archive logs
* [x] Create `tar.tmp` first and then change to `.tar`
* [x] Check paths: Mediation archive `temp`, `archive_logs`, `originals`, `tar_archives` and application logs
* [x] Option to move or delete the originals
* [x] Select date for TAR creation
* [x] Handle valid files in arch01 - TAR filename starts with dash `-`
* [x] Handle weird filenames (with spaces)
* [x] Make sure the application cannot run more than once at a time
* [x] Process directory after directory instead of creating complete archive list at the start
* [x] Prevent duplicate TAR file
  * If the file exists in temp, it is not created
  * If the file exists in TAR directory, it is created in temp but not transferred

### Extra

* [ ] Do not preserve original path in TAR files?
* [ ] Provide restore application
* [ ] Provide statistics script for OPS
  * [ ] Query: How many files were collected by `ICS|*_SSS` between 02:00 and 03:00
* [ ] Logs directory structure mirrors TAR - If the operations team prefers it
* [ ] Do not prefix TAR files in root with dash `-`
* [x] Universal `prepare_test_data.py`, currently limited to Zdenek and Mediation servers

### Clean Code

* [x] Refactor `archive_paths.py`
* [ ] Common static functions (e.g. `validate_path`)
* [ ] Unit test IO operations (create, rename, move, delete file)
* [ ] File handler
  * [ ] Action with originals: move or delete
  * [ ] Creating TAR
  * [ ] Creating logs
* [ ] TAR distributor
