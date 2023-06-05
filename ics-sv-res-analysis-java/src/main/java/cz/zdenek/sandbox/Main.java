package cz.zdenek.sandbox;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class Main {
    private static final String SV_EXPORTS_DIRECTORY = "c:/Zdenek/_tmp/A4A1-15618_ICS-SV_520_Reprocessing/exports";

    public static void main(String[] args) throws IOException {
        System.out.println("Started");
        for (String filename : listFiles()) {
            processFile(Paths.get(SV_EXPORTS_DIRECTORY).resolve(filename));
        }

        System.out.println("Finished");
    }

    private static Set<String> listFiles() {
        try (Stream<Path> stream = Files.list(Paths.get(SV_EXPORTS_DIRECTORY))) {
            return stream
                    .filter(Files::isRegularFile)
                    .map(Path::getFileName)
                    .map(Path::toString)
                    .collect(Collectors.toSet());
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    private static void processFile(Path inputFile) {
        System.out.println("Process" + inputFile.toString());
        List<String> rows;
        try {
            rows = Files.lines(inputFile).toList();
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
        System.out.println(rows.size());

        Map<String, Integer> dateReport = new HashMap<String, Integer>();
        dateReport.put("a", 1);
        /*
        for (Map.Entry<String, Integer> entry : dateReport) {
            System.out.println("x");
        }
        */
    }
}