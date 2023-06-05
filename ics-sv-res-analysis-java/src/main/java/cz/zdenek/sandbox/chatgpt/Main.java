package cz.zdenek.sandbox.chatgpt;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;

public class Main {
    private static final String SV_EXPORTS_DIRECTORY = "c:/Zdenek/_tmp/A4A1-15618_ICS-SV_520_Reprocessing/exports";
    private static final String REPORTS_DIRECTORY = "c:/Zdenek/_tmp/A4A1-15618_ICS-SV_520_Reprocessing/reports_java";

    public static void main(String[] args) {
        System.out.println("Started");

        File svExportsDirectory = new File(SV_EXPORTS_DIRECTORY);
        File[] svExports = svExportsDirectory.listFiles();
        if (svExports != null) {
            for (File svExport : svExports) {
                processSvExport(svExport.getAbsolutePath(), REPORTS_DIRECTORY);
            }
        }

        System.out.println("Finished");
    }

    private static void processSvExport(String svExportFilePath, String reportsDirectoryPath) {
        System.out.println("sv_export_file_path=" + svExportFilePath);
        Report aPartyReport = new Report();
        Report dateReport = new Report();

        try (BufferedReader reader = new BufferedReader(new FileReader(svExportFilePath))) {
            String line;
            int lineCount = 0;
            while ((line = reader.readLine()) != null) {
                if (lineCount == 0 && line.split(",")[0].equals("TRACE")) {
                    lineCount++;
                    continue;
                }
                String[] row = line.split(",");
                String aParty = row[18];
                String fullPath = row[41];
                String chargeStartDate = row[44].substring(6, 10) + "-" + row[44].substring(3, 5) + "-" + row[44].substring(0, 2);
                int duration = Integer.parseInt(row[53]);
                aPartyReport.add(aParty + "," + fullPath, duration);
                dateReport.add(chargeStartDate + "," + fullPath, duration);
                lineCount++;
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

        System.out.println("a_party_report_size=" + aPartyReport.size());
        System.out.println("date_report_size=" + dateReport.size());

        String exportFilename = new File(svExportFilePath).getName().split("\\.")[0];
        try {
            aPartyReport.save(reportsDirectoryPath + "/" + exportFilename + "_a_party.csv", "A-Party");
            dateReport.save(reportsDirectoryPath + "/" + exportFilename + "_date.csv", "Date");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
