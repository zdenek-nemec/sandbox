# Intermediate Tools: Compiler

Main

* [x] `compile.sh`
* [x] `get_compile_list.py`
* [x] `README.md`

Secondary

* [ ] `functions.sh` - Currently not needed
* [ ] `set_aliases.sh` - Under construction
* [x] `tests`

Implemented in Bash and Python 3.8

Dependencies

* ...

Synopsis

```text
...
```

Examples

```text
...
```

Testing Structure (Dependencies)

* `directory` - Ignore
* `library_a`
* `library_aac`
  * `library_a`
  * `library_ac`
    * `library_a`
    * `library_c`
* `library_ac`
  * `library_a`
  * `library_c`
* `library_b`
* `library_c`
* `readme.txt` - Ignore
* `script_a`
  * `library_a`
* `script_aac`
  * `library_a`
  * `library_ac`

To Do

* [x] Allow targeting
* [x] Parameter `--all`
* [x] Continue on error
* [x] Handle unknown scripts
* [ ] Autocomplete
* [ ] Check for cyclic dependencies
* [ ] Handle h3a_common.h
* [ ] Handle records
* [ ] Print dependency list
* [ ] Better handling of unknown scripts
