package cz.zdenek.sandbox.adventofcode2022.day3;

import org.junit.Assert;
import org.junit.Test;

import java.util.Arrays;
import java.util.List;

public class RucksackTest {
    private static final List<String> RUCKSACKS = Arrays.asList(
            "vJrwpWtwJgWrhcsFMMfFFhFp",
            "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
            "PmmdzqPrVvPwwTWBwg",
            "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
            "ttgJtRGJQctTZtZT",
            "CrZsJsPPZsGzwwsLwLmpwMDw"
    );

    @Test
    public void testGetRucksackLength() {
        for (String content : RUCKSACKS) {
            Rucksack rucksack = new Rucksack(content);
            Assert.assertEquals(Integer.valueOf(content.length()), rucksack.getRucksackLength());
        }
    }

    @Test
    public void testGetCompartmentLength() {
        for (String content : RUCKSACKS) {
            Rucksack rucksack = new Rucksack(content);
            Assert.assertEquals(Integer.valueOf(content.length() / 2), rucksack.getCompartmentLength());
        }
    }

    @Test
    public void testGetFirstCompartment() {
        Rucksack rucksack = new Rucksack("vJrwpWtwJgWrhcsFMMfFFhFp");
        Assert.assertEquals("vJrwpWtwJgWr", rucksack.getLeftCompartment());
    }

    @Test
    public void testGetSecondCompartment() {
        Rucksack rucksack = new Rucksack("vJrwpWtwJgWrhcsFMMfFFhFp");
        Assert.assertEquals("hcsFMMfFFhFp", rucksack.getRightCompartment());
    }

    @Test
    public void testGetSharedItemsOfTwo() {
        Rucksack rucksack = new Rucksack("vJrwpWtwJgWrhcsFMMfFFhFp");
        Assert.assertEquals("p", rucksack.getSharedItemsOfTwo(rucksack.getLeftCompartment(), rucksack.getRightCompartment()));
    }

    @Test
    public void testGetSharedItemsOfMore() {
        Rucksack rucksack = new Rucksack("");
        List<String> group1 = RUCKSACKS.subList(0, 3);
        List<String> group2 = RUCKSACKS.subList(3, 6);
        Assert.assertEquals("r", rucksack.getSharedItemsOfMore(group1));
        Assert.assertEquals("Z", rucksack.getSharedItemsOfMore(group2));
    }

    @Test
    public void testGetPriorityOfItem() {
        Rucksack rucksack = new Rucksack("");
        Assert.assertEquals(Integer.valueOf(1), rucksack.getPriorityOfItem('a'));
        Assert.assertEquals(Integer.valueOf(27), rucksack.getPriorityOfItem('A'));
        Assert.assertEquals(Integer.valueOf(16), rucksack.getPriorityOfItem('p'));
        Assert.assertEquals(Integer.valueOf(38), rucksack.getPriorityOfItem('L'));
        Assert.assertEquals(Integer.valueOf(42), rucksack.getPriorityOfItem('P'));
        Assert.assertEquals(Integer.valueOf(22), rucksack.getPriorityOfItem('v'));
        Assert.assertEquals(Integer.valueOf(20), rucksack.getPriorityOfItem('t'));
        Assert.assertEquals(Integer.valueOf(19), rucksack.getPriorityOfItem('s'));
    }
}
