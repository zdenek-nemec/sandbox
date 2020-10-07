# JSON to CSV Converter

## To Do

...

## Dead Code

```python
def get_header(records):
    header = []
    for record in records:
        for key in record.keys():
            if not key in header:
                header.append(key)
        break
    return header

def create_csv_file(filename, records):
    header = get_header(records)
    with open(filename, "w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=",")
        csv_writer.writerow(header)
        for record in records:
            row = []
            for column in header:
                if column in record.keys():
                    row.append(record[column])
                else:
                    row.append("")
            csv_writer.writerow(row)
```
