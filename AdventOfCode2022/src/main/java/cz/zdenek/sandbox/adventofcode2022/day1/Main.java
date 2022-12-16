package cz.zdenek.sandbox.adventofcode2022.day1;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;

public class Main {
    //    private static final String INPUT_FILE = "data/day1_example.txt";
    private static final String INPUT_FILE = "data/input.txt";
    private static final int TOP_ELVES = 3;

    public static void main(String[] args) throws IOException {
        System.out.println("Day 1");

        List<String> lines = Files.readAllLines(Paths.get(INPUT_FILE));
        System.out.println("Input filename: " + INPUT_FILE);
        System.out.println("Input file lines: " + lines.size());

        Inventory inventory = new Inventory(lines);
        System.out.println("Inventory length: " + inventory.getLength());
        System.out.println("Elves: " + inventory.getElves());
        System.out.println("Elf with the most calories has " + inventory.getMostCaloriesOnElf() + " calories");
        System.out.println("Calories on top " + TOP_ELVES + " elves: " + inventory.getCaloriesOnTopXElves(TOP_ELVES));
    }
}
