package cz.zdenek.sandbox.adventofcode2022.day3;

public class Rucksack {
    private final String content;

    public Rucksack(String content) {
        this.content = content;
    }

    public Integer getRucksackLength() {
        return this.content.length();
    }

    public Integer getCompartmentLength() {
        return this.content.length() / 2;
    }

    public String getFirstCompartment() {
        return this.content.substring(0, getCompartmentLength());
    }

    public String getSecondCompartment() {
        return this.content.substring(getCompartmentLength());
    }

    public String getSharedItems() throws Exception {
        String first = getFirstCompartment();
        String second = getSecondCompartment();
        StringBuilder shared = new StringBuilder();
        for (char item : first.toCharArray()) {
            if (second.indexOf(item) != -1) {
                if (shared.toString().indexOf(item) == -1) {
                    shared.append(item);
                }
            }
        }
        if (shared.toString().length() != 1) {
            throw new Exception("Unexpected number of shared items");
        }
        return shared.toString();
    }

    public Integer getPriorityOfItem(Character item) {
        if (item >= 'a' && item <= 'z') {
            return item - 'a' + 1;
        } else {
            return item - 'A' + 27;
        }
    }
}
