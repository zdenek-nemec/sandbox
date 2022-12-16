package cz.zdenek.sandbox.adventofcode2022.day2;

import java.util.Iterator;
import java.util.List;

public class RockPaperScissorsGuide {
    private final List<String> lines;

    public RockPaperScissorsGuide(List<String> lines) {
        this.lines = lines;
    }

    public int getLength() {
        return this.lines.size();
    }

    public Integer getAllRightPoints() {
        Iterator<String> iterator = this.lines.iterator();
        Integer points = 0;
        RockPaperScissors rps = new RockPaperScissors();
        while (iterator.hasNext()) {
            points += rps.getRightPoints(iterator.next());
        }
        return points;
    }

    public Integer getAllRightPointsUpdated() {
        Iterator<String> iterator = this.lines.iterator();
        Integer points = 0;
        RockPaperScissorsUpdated rpsu = new RockPaperScissorsUpdated();
        while (iterator.hasNext()) {
            points += rpsu.getRightPoints(iterator.next());
        }
        return points;
    }
}
