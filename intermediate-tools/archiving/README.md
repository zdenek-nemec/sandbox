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

* [x] Ignore
* [ ] Refactor `archive_paths.py` - Better naming
* [ ] Monthly directories in TAR target
