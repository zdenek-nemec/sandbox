# Windows Task Disabler

## Program Files

* `windows-task-disabler`
  * `disable_task.bat`
  * `disable_task.ps1`
  * `README.md`

## Installation

1. Save all the files to the same directory
2. Update paths in `disable_task.bat`

### Windows Defender Scheduled Scan

Via Windows Task Scheduler create a new task with following settings:

* General
  * Name = Disable Windows Defender Scheduled Scan
  * Run whether user is logged or not = Selected
  * Run with highest privileges = Checked
  * Hidden = Checked
  * Configure for = Windows 10
* Triggers
  * One time = Selected
  * Repeat task every = Checked
    * 30 minutes
  * For a duration = Indefinitely
* Actions
  * Start a program
  * Program/Script = `C:\Zdenek\Git\GitHub\sandbox\powershell-windows-task-disabler\disable_task.bat`
  * Add arguments = `"Windows Defender Scheduled Scan"`
* Settings
  * Allow task to be run on demand = Checked
  * Run tash as soon as possible after a scheduled start is missed = Checked
  * Stops the task if it runs longer than = Checked
    * 1 hour
