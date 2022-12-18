package cz.zdenek.sandbox.adventofcode2022.day3;

import java.util.Iterator;
import java.util.List;

public class Rucksack {
    private final String content;
    private final String leftCompartment;
    private final String rightCompartment;

    public Rucksack(String content) {
        this.content = content;
        this.leftCompartment = content.substring(0, getCompartmentLength());
        this.rightCompartment = content.substring(getCompartmentLength());
    }

    public Integer getRucksackLength() {
        return this.content.length();
    }

    public Integer getCompartmentLength() {
        return this.content.length() / 2;
    }

    public String getLeftCompartment() {
        return this.leftCompartment;
    }

    public String getRightCompartment() {
        return this.rightCompartment;
    }

    public String getSharedItemsOfTwo(String left, String right) {
        StringBuilder shared = new StringBuilder();
        for (char item : left.toCharArray()) {
            if (right.indexOf(item) != -1) {
                if (shared.toString().indexOf(item) == -1) {
                    shared.append(item);
                }
            }
        }
        return shared.toString();
    }

    public String getSharedItemsOfMore(List<String> contents) {
        Iterator<String> iterator = contents.iterator();
        String shared = iterator.next();
        while (iterator.hasNext()) {
            shared = getSharedItemsOfTwo(shared, iterator.next());
        }
        return shared;
    }

    public Integer getPriorityOfItem(Character item) {
        if (item >= 'a' && item <= 'z') {
            return item - 'a' + 1;
        } else {
            return item - 'A' + 27;
        }
    }
}
