package cz.zdenek.sandbox.adventofcode2022.day4;

import org.junit.Assert;
import org.junit.BeforeClass;
import org.junit.Test;

import java.util.Arrays;
import java.util.List;

public class CleanupSectionAnalyzerTest {
    private static final List<String> SECTION_PAIRS = Arrays.asList(
            "2-4,6-8",
            "2-3,4-5",
            "5-7,7-9",
            "2-8,3-7",
            "6-6,4-6",
            "2-6,4-8"
    );
    private static CleanupSectionAnalyzer cleanupSectionAnalyzer;

    @BeforeClass
    public static void setUp() {
        cleanupSectionAnalyzer = new CleanupSectionAnalyzer(SECTION_PAIRS);
    }

    @Test
    public void getLength() {
        Assert.assertEquals(6, cleanupSectionAnalyzer.getLength());
    }

    @Test
    public void getFullyOverlapping() {
        Assert.assertEquals(2, cleanupSectionAnalyzer.getFullyOverlapping());
    }

    @Test
    public void getAllOverlapping() {
        Assert.assertEquals(4, cleanupSectionAnalyzer.getAllOverlapping());
    }
}
