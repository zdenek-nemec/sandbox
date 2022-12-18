package cz.zdenek.sandbox.adventofcode2022.day3;

import java.util.List;

public class RucksackAnalyzer {
    private final List<String> lines;

    public RucksackAnalyzer(List<String> lines) {
        this.lines = lines;
    }

    public int getLength() {
        return this.lines.size();
    }

    public String getAllShared() throws Exception {
        StringBuilder shared = new StringBuilder();
        for (String line : this.lines) {
            Rucksack rucksack = new Rucksack(line);
            shared.append(rucksack.getSharedItems());
        }
        return shared.toString();
    }

    public Integer getPriorities(String shared) {
        Integer totalPriorities = 0;
        Rucksack rucksack = new Rucksack("");
        for (char item : shared.toCharArray()) {
            totalPriorities += rucksack.getPriorityOfItem(item);
        }
        return totalPriorities;
    }

    public Integer getPrioritiesOfAllShared() throws Exception {
        Integer totalPriorities = 0;
        Rucksack rucksack = new Rucksack("");
        for (char item : getAllShared().toCharArray()) {
            totalPriorities += rucksack.getPriorityOfItem(item);
        }
        return totalPriorities;
    }
}
