#!/usr/bin/env python3


import ftplib
import socket
import logging
import time

from exceptions import SourceFileNotFoundError


class Collector(object):
    def __init__(self):
        self._ftp = None

    def connect(self, host, username, password, use_site_commands=True):
        logging.debug("Initiated Collector.connect()")

        if (type(host) != str
                or type(username) != str
                or type(password) != str
                or type(use_site_commands) != bool):
            logging.critical("Invalid connection request")
            raise TypeError

        logging.debug("Parameter host = %s" % host)
        logging.debug("Parameter username = %s" % username)
        logging.debug("Parameter use_site_commands = %s" % use_site_commands)

        logging.debug("Try ftplib.FTP()")
        try:
            result = self._ftp = ftplib.FTP(host)
            logging.debug("Result of ftplib.FTP() = %s" % result)
        except socket.gaierror:
            logging.error("Unknown host %s" % host)
            raise
        except TimeoutError:
            logging.error("Timeout for host %s" % host)
            raise
        except ConnectionRefusedError:
            logging.error("Connection refused for host %s" % host)
            raise
        except:
            logging.critical(
                "Unknown error - ftplib.FTP() failed while connecting to host "
                "%s" % host)
            raise
        else:
            logging.debug("Success ftplib.FTP()")

        logging.debug("Try ftplib.login()")
        try:
            result = self._ftp.login(username, password)
            logging.debug("Result of ftplib.login() = %s" % result)
        except ftplib.error_perm:
            logging.error("Cannot login as %s to %s" % (username, host))
            self._ftp.quit()
            raise
        except:
            logging.critical(
                "Unknown error - ftplib.login() failed while connecting as %s "
                "to %s" % (username, host))
            self._ftp.quit()
            raise
        else:
            logging.debug("Success ftplib.login()")

        logging.debug("Try ftplib.set_pasv(False)")
        try:
            self._ftp.set_pasv(False)
        except:
            logging.critical(
                "Unknown error - ftplib.set_pasv(False) failed while "
                "connected as %s to %s" % (username, host))
            self._ftp.quit()
            raise
        else:
            logging.debug("Success ftplib.set_pasv(False)")

        if use_site_commands:
            logging.debug("Try ftplib.voidcmd(\"site zipon\")")
            try:
                result = self._ftp.voidcmd("site zipon")
                logging.debug(
                    "Result of ftplib.voidcmd(\"site zipon\") = %s" % result)
            except:
                logging.critical(
                    "Unknown error - ftplib.voidcmd(\"site zipon\") failed "
                    "while connected as %s to %s" % (username, host))
                self._ftp.quit()
                raise
            else:
                logging.debug("Success ftplib.voidcmd(\"site zipon\")")

        logging.debug("Try ftplib.voidcmd(\"TYPE I\")")
        try:
            result = self._ftp.voidcmd("TYPE I")
            logging.debug("Result of ftplib.voidcmd(\"TYPE I\") = %s" % result)
        except:
            logging.critical(
                "Unknown error - ftplib.voidcmd(\"TYPE I\") failed while "
                "connected as %s to %s" % (username, host))
            self._ftp.quit()
            raise
        else:
            logging.debug("Success ftplib.voidcmd(\"TYPE I\")")

        if use_site_commands:
            logging.debug("Try ftplib.voidcmd(\"site srctype bin\")")
            try:
                result = self._ftp.voidcmd("site srctype bin")
                logging.debug(
                    "Result of ftplib.voidcmd(\"site srctype bin\") = %s"
                    % result)
            except:
                logging.critical(
                    "Unknown error - ftplib.voidcmd(\"site srctype bin\") "
                    "failed while connected as %s to %s" % (username, host))
                self._ftp.quit()
                raise
            else:
                logging.debug("Success ftplib.voidcmd(\"site srctype bin\")")

        logging.debug("Finished Collector.connect()")

    def disconnect(self):
        logging.debug("Initiated Collector.disconnect()")
        self._ftp.quit()
        logging.debug("Finished Collector.disconnect()")

    def download(self, filename, source_path, destination_path):
        logging.debug("Initiated Collector.download()")

        if (type(filename) != str
                or type(source_path) != str
                or type(destination_path) != str):
            logging.critical("Invalid download request")
            raise TypeError

        logging.debug("Parameter filename = %s" % filename)
        logging.debug("Parameter source_path = %s" % source_path)
        logging.debug("Parameter destination_path = %s" % destination_path)

        logging.debug("Try ftplib.cwd(source_path)")
        try:
            result = self._ftp.cwd(source_path)
            logging.debug("Result of ftplib.cwd(source_path) = %s" % result)
        except ftplib.error_perm:
            logging.error("Source directory %s does not exist" % source_path)
            raise
        except:
            logging.critical(
                "Unknown error - ftplib.cwd(source_path) failed when "
                "accessing %s" % source_path)
            raise
        else:
            logging.debug("Success ftplib.cwd(source_path)")

        for attempt in ["First", "Second", "Third"]:
            logging.debug("Try ftplib.retrbinary()")
            try:
                logging.debug("%s download attempt" % attempt)
                result = self._ftp.retrbinary(
                    "RETR " + filename,
                    open(destination_path + "/" + filename, "wb").write)
                logging.debug("Result of ftplib.retrbinary(): %s" % result)
            except ftplib.error_perm:
                logging.warning(
                    "Target file %s does not exist in source directory %s"
                    % (filename, source_path))
                raise SourceFileNotFoundError
            except FileNotFoundError as e:
                logging.debug("Exception: %s" % str(e))
                logging.error(
                    "Destination directory %s does not exist"
                    % destination_path)
                raise
            except ftplib.error_temp as e:
                logging.debug("Exception: %s" % str(e))
                if str(e)[:3] == "425":
                    logging.warning(
                        "%s attempt to collect file %s failed"
                        % (attempt, filename))
                    if attempt in ["First", "Second"]:
                        logging.info(
                            "Waiting 5 seconds before another attempt")
                        time.sleep(5)
                else:
                    logging.critical(
                        "Unknown error - ftplib.retrbinary() failed when "
                        "collecting %s from %s to %s"
                        % (filename, source_path, destination_path))
                    raise
            except:
                logging.critical(
                    "Unknown error - ftplib.retrbinary() failed when "
                    "collecting %s from %s to %s"
                    % (filename, source_path, destination_path))
                raise
            else:
                logging.debug(
                    "%s attempt to collect file %s succeeded"
                    % (attempt, filename))
                logging.debug("Success ftplib.retrbinary()")
                break
        else:
            logging.error(
                "Cannot build data connection for file %s" % filename)
            raise CannotBuildDataConnectionError

        logging.debug("Finished Collector.download()")

    def delete(self, filename, path):
        logging.debug("Initiated Collector.delete()")

        if type(filename) != str or type(path) != str:
            logging.critical("Invalid delete request")
            raise TypeError

        logging.debug("Parameter filename: %s" % filename)
        logging.debug("Parameter path: %s" % path)

        logging.debug("Try ftplib.cwd()")
        try:
            result = self._ftp.cwd(path)
            logging.debug("Result of ftplib.cwd() = %s" % result)
        except ftplib.error_perm:
            logging.error("Target directory %s does not exist" % path)
            raise
        except:
            logging.critical(
                "Unknown error - ftplib.cwd() failed when accessing %s" % path)
            raise
        else:
            logging.debug("Success ftplib.cwd()")

        for attempt in ["First", "Second"]:
            logging.debug("Try ftplib.delete()")
            try:
                result = self._ftp.delete(filename)
                logging.debug("Result of ftplib.delete() = %s" % result)
            except ftplib.error_perm:
                logging.error(
                    "Cannot delete the file %s from %s" % (filename, path))
                raise
            except:
                logging.critical(
                    "Unknown error - ftplib.delete() failed for file %s in %s"
                    % (filename, path))
                raise
            else:
                logging.debug("Success ftplib.delete()")

            if result.split(" ")[0] == "250":
                logging.debug(
                    "%s delete attempt for file %s succeeded"
                    % (attempt, filename))
                break
            else:
                logging.warning(
                    "%s delete attempt for file %s failed"
                    % (attempt, filename))
        else:
            logging.error("Both delete attempts failed")

        logging.debug("Finished Collector.delete()")


if __name__ == "__main__":
    pass
