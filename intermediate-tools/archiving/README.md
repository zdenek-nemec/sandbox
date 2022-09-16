# Intermediate Tools: Archiving

Main module: `archive.py`

Implemented in Python 3.8

Dependencies

* `parameterized`

Synopsis

```text
archive.py [--live]
```

Examples

```text
archive.py
archive.py --live
```

Structure

* `.gitignore` - Git configuration file (ignored files)
* `README.md`
* `archive.py` - Main module
* `archive_paths.py`
* `archive_target.py`
* `gimme_files.py`
* `prepare_test_data.py`
* `test_archive_paths.py`

To Do

* [x] Exclusions
* [ ] Refactor `archive_paths.py` - Better naming
* [x] Monthly directories in TAR target
* [x] Monthly directories in `logs`
* [ ] Logs directory structure will mirror TAR
* [ ] Create `tar.tmp` first and then change to `.tar`
* [ ] Provide statistics script for OPS
  * [ ] How many files were collected by `ICS|*_SSS` between 02:00 and 03:00
* [ ] Option to preserve or delete originals
* [ ] Select date (and time) for TAR creation
* [ ] Check paths: archive `logs`, `originals`, `tar`, `temp` and application logs
* [ ] What if there is valid file in arch01?
* [ ] Weird filenames (with spaces)

Installation

```text
# TAR Archiving
  15           *     *        *       *        /appl/dcs/data01/SOFTWARE/Tools/Archiving/archive.sh
```
