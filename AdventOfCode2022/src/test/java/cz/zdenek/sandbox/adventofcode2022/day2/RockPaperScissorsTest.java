package cz.zdenek.sandbox.adventofcode2022.day2;

import org.junit.AfterClass;
import org.junit.Assert;
import org.junit.BeforeClass;
import org.junit.Test;

public class RockPaperScissorsTest {
    private static RockPaperScissors RPS;

    @BeforeClass
    public static void setUp() {
        RPS = new RockPaperScissors();
    }

    @AfterClass
    public static void finished() {
    }

    @Test
    public void testGetPoints() {
        Assert.assertEquals(Integer.valueOf(1), RPS.getPoints('A'));
        Assert.assertEquals(Integer.valueOf(2), RPS.getPoints('B'));
        Assert.assertEquals(Integer.valueOf(3), RPS.getPoints('C'));
        Assert.assertEquals(Integer.valueOf(1), RPS.getPoints('X'));
        Assert.assertEquals(Integer.valueOf(2), RPS.getPoints('Y'));
        Assert.assertEquals(Integer.valueOf(3), RPS.getPoints('Z'));
    }

    @Test
    public void testGetResult() {
        Assert.assertEquals(MatchResult.Result.DRAW, RPS.getResult("A X"));
        Assert.assertEquals(MatchResult.Result.RIGHT_WINS, RPS.getResult("A Y"));
        Assert.assertEquals(MatchResult.Result.LEFT_WINS, RPS.getResult("A Z"));
        Assert.assertEquals(MatchResult.Result.LEFT_WINS, RPS.getResult("B X"));
        Assert.assertEquals(MatchResult.Result.DRAW, RPS.getResult("B Y"));
        Assert.assertEquals(MatchResult.Result.RIGHT_WINS, RPS.getResult("B Z"));
        Assert.assertEquals(MatchResult.Result.RIGHT_WINS, RPS.getResult("C X"));
        Assert.assertEquals(MatchResult.Result.LEFT_WINS, RPS.getResult("C Y"));
        Assert.assertEquals(MatchResult.Result.DRAW, RPS.getResult("C Z"));
    }

    @Test
    public void testGetRightPoints() {
        Assert.assertEquals(Integer.valueOf(3 + 1), RPS.getRightPoints("A X"));
        Assert.assertEquals(Integer.valueOf(6 + 2), RPS.getRightPoints("A Y"));
        Assert.assertEquals(Integer.valueOf(0 + 3), RPS.getRightPoints("A Z"));
        Assert.assertEquals(Integer.valueOf(0 + 1), RPS.getRightPoints("B X"));
        Assert.assertEquals(Integer.valueOf(3 + 2), RPS.getRightPoints("B Y"));
        Assert.assertEquals(Integer.valueOf(6 + 3), RPS.getRightPoints("B Z"));
        Assert.assertEquals(Integer.valueOf(6 + 1), RPS.getRightPoints("C X"));
        Assert.assertEquals(Integer.valueOf(0 + 2), RPS.getRightPoints("C Y"));
        Assert.assertEquals(Integer.valueOf(3 + 3), RPS.getRightPoints("C Z"));
    }
}
