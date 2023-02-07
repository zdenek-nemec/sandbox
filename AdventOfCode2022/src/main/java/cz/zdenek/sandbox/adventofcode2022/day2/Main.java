package cz.zdenek.sandbox.adventofcode2022.day2;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;

public class Main {
    private static final String INPUT_FILE = "data/day2_input.txt";
    public static void main(String[] args) throws IOException {
        System.out.println("Day 2");

        List<String> lines = Files.readAllLines(Paths.get(INPUT_FILE));
        System.out.println("Input filename: " + INPUT_FILE);
        System.out.println("Input file lines: " + lines.size());

        RockPaperScissorsGuide rpsGuide = new RockPaperScissorsGuide(lines);
        System.out.println("Right player will receive " + rpsGuide.getAllRightPoints() + " points");
        System.out.println("After the update, the right player will receive " + rpsGuide.getAllRightPointsUpdated() + " points");
    }
}
