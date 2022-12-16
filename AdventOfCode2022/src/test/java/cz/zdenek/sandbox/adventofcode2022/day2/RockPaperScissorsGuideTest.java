package cz.zdenek.sandbox.adventofcode2022.day2;

import org.junit.*;

import java.util.Arrays;
import java.util.List;

public class RockPaperScissorsGuideTest {
    private static final List<String> EXAMPLE = Arrays.asList("A Y", "B X", "C Z");
    private static RockPaperScissorsGuide RPS_GUIDE;

    @BeforeClass
    public static void setUp() {
        RPS_GUIDE = new RockPaperScissorsGuide(EXAMPLE);
    }

    @AfterClass
    public static void finished() {
    }

    @Test
    public void testGetLength() {
        Assert.assertEquals(3, RPS_GUIDE.getLength());
    }

    @Test
    public void testGetAllRightPoints() {
        Assert.assertEquals(Integer.valueOf(15), RPS_GUIDE.getAllRightPoints());
    }

    @Test
    public void testGetAllRightPointsUpdated() {
        Assert.assertEquals(Integer.valueOf(12), RPS_GUIDE.getAllRightPointsUpdated());
    }
}
