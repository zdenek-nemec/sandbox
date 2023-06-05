import csv
import os.path

SV_EXPORTS_DIRECTORY = "c:/Zdenek/_tmp/A4A1-15618_ICS-SV_520_Reprocessing/exports"
REPORTS_DIRECTORY = "c:/Zdenek/_tmp/A4A1-15618_ICS-SV_520_Reprocessing/reports_python"


class Report(object):
    def __init__(self):
        self._data = {}

    def add(self, key: tuple, duration: int):
        if key not in self._data:
            self._data[key] = duration
        else:
            self._data[key] += duration

    def size(self):
        return len(self._data)

    def save(self, path: str, key_column: str = "Key"):
        with open(path, "w", newline="") as csv_file:
            writer = csv.writer(csv_file, delimiter=",", quotechar="\"", quoting=csv.QUOTE_MINIMAL)
            writer.writerow([key_column, "Full-Path", "Duration", "Duration Converted"])
            for key in sorted(self._data.keys()):
                core_key, full_path = key
                duration = self._data[key]
                hours = duration // (60 * 60)
                minutes = (duration % (60 * 60)) // 60
                seconds = duration % 60
                if duration != hours * 60 * 60 + minutes * 60 + seconds:
                    raise RuntimeError("Duration mismatch")
                duration_converted = f"{hours}:{minutes:0>2}:{seconds:0>2}"
                writer.writerow([core_key, full_path, duration, duration_converted])


def process_sv_export(sv_export_file_path: str, reports_directory_path: str):
    print(f"{sv_export_file_path=}")
    a_party_report = Report()
    date_report = Report()
    with open(sv_export_file_path, "r") as csv_file:
        reader = csv.reader(csv_file, delimiter=",")
        for i, row in enumerate(reader):
            if i == 0 and row[0] == "TRACE":
                continue
            a_party = row[18]
            full_path = row[41]
            charge_start_date = row[44][6:10] + "-" + row[44][3:5] + "-" + row[44][0:2]
            duration = int(row[53])
            a_party_report.add((a_party, full_path), duration)
            date_report.add((charge_start_date, full_path), duration)

    print(f"{a_party_report.size()=}")
    print(f"{date_report.size()=}")

    export_filename, _ = str(os.path.basename(sv_export_file_path)).split(".")
    a_party_report.save(os.path.normpath(reports_directory_path + "/" + export_filename + "_a_party.csv"), "A-Party")
    date_report.save(os.path.normpath(reports_directory_path + "/" + export_filename + "_date.csv"), "Date")


def main():
    print("Started")

    sv_exports_directory = os.path.normpath(SV_EXPORTS_DIRECTORY)
    for sv_export in os.listdir(sv_exports_directory):
        process_sv_export(
            os.path.normpath(sv_exports_directory + "/" + sv_export),
            os.path.normpath(REPORTS_DIRECTORY)
        )

    print("Finished")


if __name__ == '__main__':
    main()
