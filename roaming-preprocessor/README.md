# Roaming Preprocessor

The goal is to have a tool which will be able to load CSV data in a given format and prepare them for Intermediate processing.

Requirements

* CSV data files are loaded and format is validated against configuration file (number of columns, maybe more)
* Multiple formats can be configured (filename mask, input/output path, action: delete, move, keep)
* Filtration is possible, based on value match in specific column, the whole record can be filtered out, configurable
* Only required columns are saved to the output file, configurable
* Session records are generated from inbound/outbound records
* Application is able to recover from failure
* Application cannot run more than once with the same configuration (port lock)

Requirement Notes

* 2G/3G has one or two messages per session? Specification unclear. For demo assuming that sessions should be assembled.
* 4G/5G has two messages per session. Assemble in the tool.
* Configurable batch: allows to load and work with more than one file in memory at once

## Design

1. Application starts, loads the configuration file and checks the lock, if port is locked, stop
2. List of eligible input files is assembled, if there are none, stop
3. If present, work (tmp/dat) file is loaded from work directory to memory
4. First of eligible input files is loaded to memory, added to work data
5. Filters are applied to newly loaded data
6. Session records are assembled from work and newly loaded data
7. Complete sessions are saved to the output file
8. Incomplete records are saved to the work directory. overwrite old work file
9. Apply action to the first input file and remove it from the list
10. Jump to step (4), now with previously second file, if there are no more files, stop

Notes

* Output filename: `refix_<timestamp>_<sequence>.csv`
* Always save files (output and work) as .tmp first and then rename them 

### Configuration File Draft

```text
[settings]
name = Roaming 2G/3G
port_lock = 12345
input_path = .
input_mask = *.dat
work_path = .
output_path = .
output_filename_prefix = roaming_2g_3g_
action = Delete
columns = 4

[columns]
timestamp = [output]
type = none
observation-domain = [output]
session-id = [key, output]

[filters]
type = ["a", "b"] -- column and values to filter
...
```

## Notes

* `.gitignore` inspired by [GitHub MOOOWOOO/py-gitignore](https://gist.github.com/MOOOWOOO/3cf91616c9f3bbc3d1339adfc707b08a)

## To Do

* [ ] Configuration `.cfg`
  * [ ] Parser
  * [ ] Validator
* [x] Logging
* [ ] Application lock
  * [x] Port lock
  * [ ] Configurable application lock
    * Allows running multiple instances which do not interfere with each other
* [ ] Separate class for data loading and saving
  * Allows implementing other interfaces, e.g. DB/stream
* [ ] Validation
  * [x] Validate number of columns
  * [ ] Configurable validation (number of columns)
  * [x] Invalid entries are removed
  * [ ] Invalid entries are saved to error file 
* [ ] Filtration
* [ ] Merging
  * [x] Merge sessions based on session ID
  * [ ] Propagate release cause to the session record
  * [ ] Validate that all the values are initiated with the opening record
* [x] Save only specific columns
  * [ ] Columns returned by `RoamingData.get_data` can be requested via parameter
  * [ ] Saved columns can be configured

### Questions

* Should we extended the validation and check column values?
* Should we implement filtration?
* How to identify opening record?
* Are the sessions (both records) limited to one file?
* Should we timeout records in `work.dat`?
