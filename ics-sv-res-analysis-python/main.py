import csv
import os.path

SV_EXPORT = "c:/Zdenek/_tmp/A4A1-15618_ICS-SV_520_Reprocessing/ics_2_sv_res_v2_session_ids.csv"
REPORT_A_PARTY = "c:/Zdenek/_tmp/A4A1-15618_ICS-SV_520_Reprocessing/reports/ics_2_sv_res_v2_session_ids_report_a_party.csv"
REPORT_DATE = "c:/Zdenek/_tmp/A4A1-15618_ICS-SV_520_Reprocessing/reports/ics_2_sv_res_v2_session_ids_report_date.csv"


class Report(object):
    def __init__(self):
        self._data = {}

    def add(self, key: str, duration: int):
        if key not in self._data:
            self._data[key] = duration
        else:
            self._data[key] += duration

    def size(self):
        return len(self._data)

    def save(self, path: str, key: str = "Key"):
        with open(path, "w", newline="") as csv_file:
            writer = csv.writer(csv_file, delimiter=",", quotechar="\"", quoting=csv.QUOTE_MINIMAL)
            writer.writerow([key, "Duration", "Duration Converted"])
            for key in sorted(self._data.keys()):
                duration = self._data[key]
                hours = duration // (60 * 60)
                minutes = (duration % (60 * 60)) // 60
                seconds = duration % 60
                if duration != hours * 60 * 60 + minutes * 60 + seconds:
                    raise RuntimeError("Duration mismatch")
                duration_converted = f"{hours}:{minutes:0>2}:{seconds:0>2}"
                writer.writerow([key, duration, duration_converted])


def main():
    print("Started")

    sv_export_file = os.path.normpath(SV_EXPORT)
    print(f"{sv_export_file=}")
    a_party_report = Report()
    date_report = Report()
    with open(sv_export_file, "r") as csv_file:
        reader = csv.reader(csv_file, delimiter=",")
        for i, row in enumerate(reader):
            if i == 0 and row[0] == "TRACE":
                continue
            a_party = row[18]
            charge_start_date = row[44][6:10] + "-" + row[44][3:5] + "-" + row[44][0:2]
            duration = int(row[53])
            a_party_report.add(a_party, duration)
            date_report.add(charge_start_date, duration)

    print(f"{a_party_report.size()=}")
    print(f"{date_report.size()=}")

    a_party_report.save(os.path.normpath(REPORT_A_PARTY), "A-Party")
    date_report.save(os.path.normpath(REPORT_DATE), "Date")

    print("Finished")


if __name__ == '__main__':
    main()
