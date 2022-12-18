package cz.zdenek.sandbox.adventofcode2022.day3;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public class RucksackAnalyzer {
    private final List<String> lines;

    public RucksackAnalyzer(List<String> lines) {
        this.lines = lines;
    }

    public int getLength() {
        return this.lines.size();
    }

    public String getAllShared() {
        StringBuilder shared = new StringBuilder();
        for (String line : this.lines) {
            Rucksack rucksack = new Rucksack(line);
            shared.append(rucksack.getSharedItemsOfTwo(rucksack.getLeftCompartment(), rucksack.getRightCompartment()));
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

    public Integer getPrioritiesOfAllShared() {
        Integer totalPriorities = 0;
        Rucksack rucksack = new Rucksack("");
        for (char item : getAllShared().toCharArray()) {
            totalPriorities += rucksack.getPriorityOfItem(item);
        }
        return totalPriorities;
    }

    public String getAllBadges() {
        Iterator<String> iterator = this.lines.iterator();
        Rucksack rucksack = new Rucksack("");
        StringBuilder badges = new StringBuilder();
        while (iterator.hasNext()) {
            List<String> group = new ArrayList<>();
            for (int i = 0; i < 3; i++) {
                group.add(iterator.next());
            }
            badges.append(rucksack.getSharedItemsOfMore(group));
        }
        return badges.toString();
    }
}
