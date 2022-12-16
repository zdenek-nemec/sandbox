package cz.zdenek.sandbox.adventofcode2022;

import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Iterator;
import java.util.List;

public class Day1 {
    public static void main(String[] args) throws IOException {
        System.out.println("Day 1");

        List<String> inventory = Files.readAllLines(Paths.get("data/day1_example.txt"));
        System.out.println("Inventory length: " + inventory.size());

        Iterator<String> inventoryIterator = inventory.iterator();
        int elves = 0;
        int calories = 0;
        Boolean isSameElf = true;
        Boolean emptyNewLine = false;
        while (inventoryIterator.hasNext()) {
            String line = inventoryIterator.next();


//            if (line.length() > 0) {
//            } else if (isSameElf) {
//            } else {
//                elves++;
//                isSameElf = true;
//                emptyNewLine =
//            }
        }
        System.out.println("Elves: " + elves);;

    }
}
