# Intermediate Tools: Compiler

Main

* `compile.sh`
* `get_compile_list.py`
* `set_aliases.sh`
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

* [ ] Check for cyclic dependencies
* [ ] Handle h3a_common.h
* [ ] Handle records
* [ ] Prompt before compiling
