# Python Without Root

## Standard Installation on Linux

1. Update APT.

    ```text
    sudo apt-get update
    ```

2. Install Python 3.

    ```text
    sudo apt-get install python3.7
    ```

### Notes

* Python 2 (`python`) is no longer supported, use Python 3.
* Many of the Linux distributions did not declare full support for Python 3.8, use Python 3.7.

---

## Portable Installation on Linux

1. Make sure the C compiler is present. If not, it must be installed (root needed).

   ```text
   sudo apt-get install gcc
   ```

2. Download preferred Python version.
    * Use `wget`

        ```text
        wget https://www.python.org/ftp/python/3.7.8/Python-3.7.8.tgz
        ```

    * Or download it from the [official website](https://www.python.org/) and deliver by other means.

3. Decompress Python files in desired directory.

    ```text
    tar -zxf Python-3.7.8.tgz
    ```

4. On the Intermediate server prevent profile setup `med_set_environment.sh` and reload the session in order to have a clean environment.

5. Go into directory with Python files and start the configuration.

    ```text
    ./configure --prefix=/appl/mediation/data01/SOFTWARE/Python-3.7.8
    ```

6. Install.

    ```text
    make && make install
    ```

7. Enable environment setup if you are on the Intermediate server.

8. Setup following variables permanently of per session whenever you need to use the Python.

    ```text
    PYTHONHOME=/appl/mediation/data01/SOFTWARE/Python-3.7.8
    PYTHONPATH=/appl/mediation/data01/SOFTWARE/Python-3.7.8/lib
    ```

9. Setup `PATH` variable if you want to use this Python version as default.
