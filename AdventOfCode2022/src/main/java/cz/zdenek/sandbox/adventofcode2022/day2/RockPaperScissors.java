package cz.zdenek.sandbox.adventofcode2022.day2;

import java.util.HashMap;

public class RockPaperScissors {
    private static final HashMap<Character, Integer> POINTS = new HashMap<>() {{
        put('A', 1); // Left rock
        put('B', 2); // Left paper
        put('C', 3); // Left scissors
        put('X', 1); // Right rock
        put('Y', 2); // Right paper
        put('Z', 3); // Right scissors
    }};
    private static final HashMap<String, MatchResult.Result> RULES = new HashMap<>() {{
        put("A X", MatchResult.Result.DRAW);
        put("A Y", MatchResult.Result.RIGHT_WINS);
        put("A Z", MatchResult.Result.LEFT_WINS);
        put("B X", MatchResult.Result.LEFT_WINS);
        put("B Y", MatchResult.Result.DRAW);
        put("B Z", MatchResult.Result.RIGHT_WINS);
        put("C X", MatchResult.Result.RIGHT_WINS);
        put("C Y", MatchResult.Result.LEFT_WINS);
        put("C Z", MatchResult.Result.DRAW);
    }};

    public RockPaperScissors() {
    }

    public Integer getPoints(Character shape) {
        return POINTS.get(shape);
    }

    public MatchResult.Result getResult(String match) {
        return RULES.get(match);
    }

    public Integer getRightPoints(String match) {
        MatchResult.Result matchResult = getResult(match);
        Integer points = getPoints(match.charAt(2));
        if (matchResult.equals(MatchResult.Result.RIGHT_WINS)) {
            return points + 6;
        } else if (matchResult.equals(MatchResult.Result.DRAW)) {
            return points + 3;
        } else {
            return points + 0;
        }
    }
}
