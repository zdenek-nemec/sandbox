package cz.zdenek.sandbox.adventofcode2022.day3;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;

public class Main {
    private static final String INPUT_FILE = "data/day3_input.txt";

    public static void main(String[] args) throws IOException {
        System.out.println("Day 3");

        List<String> lines = Files.readAllLines(Paths.get(INPUT_FILE));
        System.out.println("Input filename: " + INPUT_FILE);
        System.out.println("Input file lines: " + lines.size());
    }
}
