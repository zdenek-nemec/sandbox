package cz.zdenek.sandbox.adventofcode2022.day2;

import java.util.HashMap;

public class RockPaperScissorsUpdated {
    // X = loss, Y = draw, Z = win
    private static final HashMap<String, Integer> MATCH_POINTS = new HashMap<>() {{
        put("A X", 3);
        put("A Y", 1 + 3);
        put("A Z", 2 + 6);
        put("B X", 1);
        put("B Y", 2 + 3);
        put("B Z", 3 + 6);
        put("C X", 2);
        put("C Y", 3 + 3);
        put("C Z", 1 + 6);
    }};

    public Integer getRightPoints(String match) {
        return MATCH_POINTS.get(match);
    }
}
