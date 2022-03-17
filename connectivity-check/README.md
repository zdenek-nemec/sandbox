# Connectivity Check

## Usage

```bash
run.sh
```

## Intermediate 9

```text
# Connectivity Check
55 */4 * * * . /dcs/data01/SOFTWARE/Tools/med_set_environment_v9.sh 2>&1; /dcs/data01/SOFTWARE/Tools/ConnectivityCheck/run.sh > /dcs/data01/SOFTWARE/Tools/ConnectivityCheck/results/connectivity_check_`date '+\%Y-\%m-\%d_\%H-\%M-\%S'`.csv
```
