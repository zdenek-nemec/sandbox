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
    public void getAllShared() throws Exception {
        Assert.assertEquals("pLPvts", rucksackAnalyzer.getAllShared());
    }

    @Test
    public void getPriorities() throws Exception {
        Assert.assertEquals(Integer.valueOf(157), rucksackAnalyzer.getPriorities(rucksackAnalyzer.getAllShared()));
    }

    @Test
    public void getPrioritiesOfAllShared() throws Exception {
        Assert.assertEquals(Integer.valueOf(157), rucksackAnalyzer.getPrioritiesOfAllShared());
    }
}
