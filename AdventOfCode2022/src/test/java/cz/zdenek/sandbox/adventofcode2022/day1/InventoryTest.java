package cz.zdenek.sandbox.adventofcode2022.day1;

import junit.framework.TestCase;

import java.util.Arrays;
import java.util.Hashtable;
import java.util.List;

public class InventoryTest extends TestCase {
    private static final String[] LINES_EMPTY = {"", "", ""};
    private static final String[] LINES_SINGLE_ELF = {"1", "2", "3"};
    private static final String[] LINES_SINGLE_ELF_NEWLINE = {"1", "2", "3", ""};
    private static final String[] LINES_MULTIPLE_ELVES = {"1", "2", "3", "", "1"};
    private static final String[] LINES_MULTIPLE_ELVES_NEWLINE = {"1", "2", "3", "", "1", ""};
    private static final String[] LINES_MULTIPLE_ELVES_MULTIPLE_MID_NEWLINES = {"1", "2", "3", "", "", "1", ""};
    private static final String[] LINES_MULTIPLE_ELVES_MULTIPLE_END_NEWLINES = {"1", "2", "3", "", "1", "", ""};

    private static final String[] LINES_EXAMPLE = {"1000", "2000", "3000", "", "4000", "", "5000", "6000", "", "7000", "8000", "9000", "", "10000"};
    private static final int EXPECTED_ELVES_IN_LINES_EXAMPLE = 5;

    // Test getLength

    public void testGetLengthEmptyLines() {
        List<String> lines = Arrays.asList(LINES_EMPTY);
        Inventory inventory = new Inventory(lines);
        assertEquals(LINES_EMPTY.length, inventory.getLength());
    }

    public void testGetLengthSingleElf() {
        List<String> lines = Arrays.asList(LINES_SINGLE_ELF);
        Inventory inventory = new Inventory(lines);
        assertEquals(LINES_SINGLE_ELF.length, inventory.getLength());
    }

    public void testGetLengthSingleElfNewline() {
        List<String> lines = Arrays.asList(LINES_SINGLE_ELF_NEWLINE);
        Inventory inventory = new Inventory(lines);
        assertEquals(LINES_SINGLE_ELF_NEWLINE.length, inventory.getLength());
    }

    public void testGetLengthMultipleElves() {
        List<String> lines = Arrays.asList(LINES_MULTIPLE_ELVES);
        Inventory inventory = new Inventory(lines);
        assertEquals(LINES_MULTIPLE_ELVES.length, inventory.getLength());
    }

    public void testGetLengthMultipleElvesNewline() {
        List<String> lines = Arrays.asList(LINES_MULTIPLE_ELVES_NEWLINE);
        Inventory inventory = new Inventory(lines);
        assertEquals(LINES_MULTIPLE_ELVES_NEWLINE.length, inventory.getLength());
    }

    public void testGetLengthExample() {
        List<String> lines = Arrays.asList(LINES_EXAMPLE);
        Inventory inventory = new Inventory(lines);
        assertEquals(LINES_EXAMPLE.length, inventory.getLength());
    }

    // Test getElves

    public void testGetElvesEmptyLines() {
        List<String> lines = Arrays.asList(LINES_EMPTY);
        Inventory inventory = new Inventory(lines);
        assertEquals(0, inventory.getElves());
    }

    public void testGetElvesSingleElf() {
        List<String> lines = Arrays.asList(LINES_SINGLE_ELF);
        Inventory inventory = new Inventory(lines);
        assertEquals(1, inventory.getElves());
    }

    public void testGetElvesSingleElfNewline() {
        List<String> lines = Arrays.asList(LINES_SINGLE_ELF_NEWLINE);
        Inventory inventory = new Inventory(lines);
        assertEquals(1, inventory.getElves());
    }

    public void testGetElvesMultipleElves() {
        List<String> lines = Arrays.asList(LINES_MULTIPLE_ELVES);
        Inventory inventory = new Inventory(lines);
        assertEquals(2, inventory.getElves());
    }

    public void testGetElvesMultipleElvesNewline() {
        List<String> lines = Arrays.asList(LINES_MULTIPLE_ELVES_NEWLINE);
        Inventory inventory = new Inventory(lines);
        assertEquals(2, inventory.getElves());
    }

    public void testGetElvesMultipleElvesMultipleMidNewlines() {
        List<String> lines = Arrays.asList(LINES_MULTIPLE_ELVES_MULTIPLE_MID_NEWLINES);
        Inventory inventory = new Inventory(lines);
        assertEquals(2, inventory.getElves());
    }

    public void testGetElvesMultipleElvesMultipleEndNewlines() {
        List<String> lines = Arrays.asList(LINES_MULTIPLE_ELVES_MULTIPLE_END_NEWLINES);
        Inventory inventory = new Inventory(lines);
        assertEquals(2, inventory.getElves());
    }

    public void testGetElvesExample() {
        Inventory inventory = new Inventory(Arrays.asList(LINES_EXAMPLE));
        assertEquals(EXPECTED_ELVES_IN_LINES_EXAMPLE, inventory.getElves());
    }

    // Test getCaloriesPerElf

    public void testGetCaloriesPerElfMultipleElves() {
        Inventory inventory = new Inventory(Arrays.asList(LINES_MULTIPLE_ELVES));
        Hashtable<Integer, Integer> expectedResult = new Hashtable<>();
        expectedResult.put(0, 6);
        expectedResult.put(1, 1);
        assertEquals(expectedResult, inventory.getCaloriesPerElf());
    }

    public void testGetCaloriesPerElfMultipleElvesNewline() {
        Inventory inventory = new Inventory(Arrays.asList(LINES_MULTIPLE_ELVES_NEWLINE));
        Hashtable<Integer, Integer> expectedResult = new Hashtable<>();
        expectedResult.put(0, 6);
        expectedResult.put(1, 1);
        assertEquals(expectedResult, inventory.getCaloriesPerElf());
    }

    public void testGetCaloriesPerElfExample() {
        Inventory inventory = new Inventory(Arrays.asList(LINES_EXAMPLE));
        Hashtable<Integer, Integer> expectedResult = new Hashtable<>();
        expectedResult.put(0, 6000);
        expectedResult.put(1, 4000);
        expectedResult.put(2, 11000);
        expectedResult.put(3, 24000);
        expectedResult.put(4, 10000);
        assertEquals(expectedResult, inventory.getCaloriesPerElf());
    }

    // Test getMostCaloriesOnElf

    public void testGetMostCaloriesOnElfMultipleElves() {
        Inventory inventory = new Inventory(Arrays.asList(LINES_MULTIPLE_ELVES));
        assertEquals(Integer.valueOf(6), inventory.getMostCaloriesOnElf());
    }

    public void testGetMostCaloriesOnElfExample() {
        Inventory inventory = new Inventory(Arrays.asList(LINES_EXAMPLE));
        assertEquals(Integer.valueOf(24000), inventory.getMostCaloriesOnElf());
    }

    // Test getCaloriesOnTopXElves

    public void testGetCaloriesOnTopXElvesExample() {
        Inventory inventory = new Inventory(Arrays.asList(LINES_EXAMPLE));
        assertEquals(Integer.valueOf(45000), inventory.getCaloriesOnTopXElves(3));
    }
}
