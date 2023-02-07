package cz.zdenek.sandbox.adventofcode2022.day3;

import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;

import java.util.Arrays;
import java.util.List;

public class RucksackAnalyzerTest {
    private static final List<String> RUCKSACKS = Arrays.asList(
            "vJrwpWtwJgWrhcsFMMfFFhFp",
            "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
            "PmmdzqPrVvPwwTWBwg",
            "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
            "ttgJtRGJQctTZtZT",
            "CrZsJsPPZsGzwwsLwLmpwMDw"
    );
    private static RucksackAnalyzer rucksackAnalyzer;

    @Before
    public void setUp() {
        rucksackAnalyzer = new RucksackAnalyzer(RUCKSACKS);
    }

    @Test
    public void getLength() {
        Assert.assertEquals(RUCKSACKS.size(), rucksackAnalyzer.getLength());
    }

    @Test
    public void getAllShared() {
        Assert.assertEquals("pLPvts", rucksackAnalyzer.getAllShared());
    }

    @Test
    public void getPriorities() {
        Assert.assertEquals(Integer.valueOf(157), rucksackAnalyzer.getPriorities(rucksackAnalyzer.getAllShared()));
        Assert.assertEquals(Integer.valueOf(70), rucksackAnalyzer.getPriorities(rucksackAnalyzer.getAllBadges()));
    }

    @Test
    public void getPrioritiesOfAllShared() {
        Assert.assertEquals(Integer.valueOf(157), rucksackAnalyzer.getPrioritiesOfAllShared());
    }

    @Test
    public void getAllBadges() {
        Assert.assertEquals("rZ", rucksackAnalyzer.getAllBadges());
    }
}
