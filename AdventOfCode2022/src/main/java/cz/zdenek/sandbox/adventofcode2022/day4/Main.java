package cz.zdenek.sandbox.adventofcode2022.day4;

import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;

public class Main {
    private static final String INPUT_FILE = "data/day4_input.txt";

    public static void main(String[] args) throws Exception {
        System.out.println("Day 4");

        List<String> lines = Files.readAllLines(Paths.get(INPUT_FILE));
        System.out.println("Input filename: " + INPUT_FILE);
        System.out.println("Input file lines: " + lines.size());

        CleanupSectionAnalyzer cleanupSectionAnalyzer = new CleanupSectionAnalyzer(lines);
        System.out.println("Fully overlapping: " + cleanupSectionAnalyzer.getFullyOverlapping());
        System.out.println("All overlapping: " + cleanupSectionAnalyzer.getAllOverlapping());
    }
}
