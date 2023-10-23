# Helios Mock

Mock applications for testing Aiviro on Helios.

Mocks:

* `hg_2vv.py` - Mock for Helios Green 2VV invoice detail
* `hn_epl.py` - Mock for Helios Nephrite EPL invoice detail

## Install

1. Install Python 3.11+ with Tkinter
2. Run relevant application

## Deploy on Windows without Admin

Have Python installed somewhere else, so you can procure Tkinter files.

1. Download Python Windows embedable package from [www.python.org](https://www.python.org/) and unzip it locally

2. Copy following directories and files from the installed version to the embedable package

  ```text
  Python-3.11-64-installed/tcl/*             -> Python-3.11-64-embedded/tcl/
  Python-3.11-64-installed/Lib/tkinter/*     -> Python-3.11-64-embedded/tkinter/
  Python-3.11-64-installed/DLLs/_tkinter.pyd -> Python-3.11-64-embedded/
  Python-3.11-64-installed/DLLs/tcl86t.dll   -> Python-3.11-64-embedded/
  Python-3.11-64-installed/DLLs/tk86t.dll    -> Python-3.11-64-embedded/
  ```

3. Run Python via `Python-3.11-64-embedded/python.exe`

Sources

* [Stack Overflow](https://stackoverflow.com/questions/37710205/python-embeddable-zip-install-tkinter)

## Todo

* [ ] Windows batch file for running the mock application
* [x] `green_2vv_order_detail.py`
