package cz.zdenek.sandbox.adventofcode2022.day4;

import java.util.List;

public class CleanupSectionAnalyzer {
    private final List<String> lines;

    public CleanupSectionAnalyzer(List<String> lines) {
        this.lines = lines;
    }

    public int getLength() {
        return this.lines.size();
    }

    public int getFullyOverlapping() {
        int fullyOverlapping = 0;
        for (String cleanupPair : lines) {
            String[] pair = cleanupPair.split(",");
            CleanupSection cleanupSection = new CleanupSection(pair[0]);
            if (cleanupSection.isOverlappingFully(pair[pair.length - 1])) {
                fullyOverlapping++;
            }
        }
        return fullyOverlapping;
    }

    public int getAllOverlapping() {
        int overlapping = 0;
        for (String cleanupPair : lines) {
            String[] pair = cleanupPair.split(",");
            CleanupSection cleanupSection = new CleanupSection(pair[0]);
            if (cleanupSection.isOverlapping(pair[pair.length - 1])) {
                overlapping++;
            }
        }
        return overlapping;
    }
}
