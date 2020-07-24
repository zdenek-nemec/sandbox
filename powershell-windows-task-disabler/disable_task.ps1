param(
    [string]$task_name
)

$task_state = (Get-ScheduledTask -TaskName $task_name).State
$timestamp = Get-Date -Format "yyyy-MM-dd HH:mm"
Write-Output "$timestamp - $task_name task status is $task_state"
if ($task_state -ne "Disabled") {
    Write-Output "$timestamp - Disabling the task $task_name"
    Get-ScheduledTask -TaskName $task_name | Disable-ScheduledTask > $null
}
