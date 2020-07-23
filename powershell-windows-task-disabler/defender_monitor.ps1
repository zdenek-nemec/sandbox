$task_name = "Windows Defender Scheduled Scan"
$task_state = (Get-ScheduledTask -TaskName $task_name).State
$timestamp = Get-Date -Format "yyyy-MM-dd HH:mm"
Write-Output "$timestamp - $task_name task status = $task_state"
