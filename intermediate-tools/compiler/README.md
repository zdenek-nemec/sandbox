# Intermediate Tools: Compiler

Main

* `compile.sh`
* `set_aliases.sh`
* `get_compile_list.py`
* `README.md`

Secondary

* `functions.sh`
* `tests`

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
* [ ] Check for cyclic dependencies
* [ ] Handle h3a_common.h
* [ ] Handle records
* [ ] Prompt before compiling
* [ ] Print list
* [ ] Warn about unknown scripts
