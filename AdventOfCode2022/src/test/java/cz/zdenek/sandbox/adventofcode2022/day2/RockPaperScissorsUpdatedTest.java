package cz.zdenek.sandbox.adventofcode2022.day2;

import org.junit.AfterClass;
import org.junit.Assert;
import org.junit.BeforeClass;
import org.junit.Test;

public class RockPaperScissorsUpdatedTest {
    private static RockPaperScissorsUpdated RPSU;

    @BeforeClass
    public static void setUp() {
        RPSU = new RockPaperScissorsUpdated();
    }

    @AfterClass
    public static void finished() {
    }

    @Test
    public void testGetRightPoints() {
        Assert.assertEquals(Integer.valueOf(0 + 3), RPSU.getRightPoints("A X"));
        Assert.assertEquals(Integer.valueOf(3 + 1), RPSU.getRightPoints("A Y"));
        Assert.assertEquals(Integer.valueOf(6 + 2), RPSU.getRightPoints("A Z"));
        Assert.assertEquals(Integer.valueOf(0 + 1), RPSU.getRightPoints("B X"));
        Assert.assertEquals(Integer.valueOf(3 + 2), RPSU.getRightPoints("B Y"));
        Assert.assertEquals(Integer.valueOf(6 + 3), RPSU.getRightPoints("B Z"));
        Assert.assertEquals(Integer.valueOf(0 + 2), RPSU.getRightPoints("C X"));
        Assert.assertEquals(Integer.valueOf(3 + 3), RPSU.getRightPoints("C Y"));
        Assert.assertEquals(Integer.valueOf(6 + 1), RPSU.getRightPoints("C Z"));
    }
}
