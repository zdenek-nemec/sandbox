package cz.zdenek.sandbox.adventofcode2022.day3;

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

    public String getSharedItems() throws Exception {
        String left = getLeftCompartment();
        String right = getRightCompartment();
        StringBuilder shared = new StringBuilder();
        for (char item : left.toCharArray()) {
            if (right.indexOf(item) != -1) {
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
