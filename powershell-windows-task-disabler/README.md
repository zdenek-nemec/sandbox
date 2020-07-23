# Defender Monitor

## Program Files

* `defender-monitor`
  * `defender_monitor.bat`
  * `defender_monitor.ps1`
  * `README.md`

## Installation

1. Save all the files to the same directory
2. Update paths in `defender_monitor.bat`
3. Create following task under Windows Task Scheduler
    * General > Name: Defender Monitor
    * General > When running the task, use SYSTEM user
    * General > Hidden
    * Triggers
      * One time
      * 0:00
      * Repeat task every 30 minutes
    * Actions
      * Start a program
      * `c:\<path>\defender-monitor\defender_monitor.bat`
