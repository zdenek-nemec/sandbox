# Intermediate Synchronisation

## To Do

* [ ] `export_streams.sh`
  * [ ] Script exports all Intermediate business logics
  * [ ] Script contains documentation and supports `--help` option
* [ ] `export_tables.sh`
  * [ ] Script exports all Intermediate reference tables
  * [ ] Script contains documentation and supports `--help` option
* [ ] Automatic reference table updates

## Structure

`intermediate-synchronisation`
├─ `check_synchrinosation.py`
├─ `export_streams.sh`
├─ `export_tables.sh`
├─ `run.sh`
└─ `README.md`

## Description

Cronjobs run Bash scripts `export_*.sh` on regular basis on both Intermediate production and stanby servers. Bash script `run.sh` start Python 3 script `check_synchrinosation.py` which collects necessary files from both servers, compares them and reports differences.

All production features must be present on standby server and match.

Features:

* Business logics
* Bash scripts
* GDC scripts
* Reference tables
  * At least presence and number of entries
  * Ideally the content might be checked as well
  * Ideally check can be configured per table: skip, size, content
* Portals
  * Presence of the portal is checked
  * Basic configuration (e.g. root tab) is checked
  * Routing, Output and Dispatch tabs do not have to be checked due to reprocessing
