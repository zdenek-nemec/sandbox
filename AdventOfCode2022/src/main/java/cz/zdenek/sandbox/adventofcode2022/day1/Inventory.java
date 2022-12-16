package cz.zdenek.sandbox.adventofcode2022.day1;

import java.util.Hashtable;
import java.util.Iterator;
import java.util.List;
import java.util.Set;

public class Inventory {
    private final List<String> lines;

    public Inventory(List<String> lines) {
        this.lines = lines;
    }

    public int getLength() {
        return this.lines.size();
    }

    public int getElves() {
        Iterator<String> iterator = lines.iterator();
        int elves = 0;
        boolean isSame = false;
        while (iterator.hasNext()) {
            String line = iterator.next();
            if (line.length() > 0 && !isSame) {
                elves++;
                isSame = true;
            } else if (line.length() == 0) {
                isSame = false;
            }
        }
        return elves;
    }

    public Hashtable<Integer, Integer> getCaloriesPerElf() {
        Hashtable<Integer, Integer> caloriesPerElf = new Hashtable<Integer, Integer>();
        Iterator<String> iterator = this.lines.iterator();
        Integer elves = -1;
        boolean isSame = false;
        while (iterator.hasNext()) {
            String line = iterator.next();
            if (line.length() > 0 && !isSame) {
                elves++;
                isSame = true;
                caloriesPerElf.put(elves, Integer.valueOf(line));
            } else if (line.length() == 0) {
                isSame = false;
            } else {
                caloriesPerElf.put(elves, caloriesPerElf.get(elves) + Integer.valueOf(line));
            }
        }
        return caloriesPerElf;
    }

    public Integer getMostCaloriesOnElf() {
        Hashtable<Integer, Integer> caloriesPerElf = getCaloriesPerElf();
        Set<Integer> keys = caloriesPerElf.keySet();
        Integer maximumCaloriesPerElf = 0;
        for (Integer key: keys) {
            Integer caloriesOnThisElf = caloriesPerElf.get(key);
            if (caloriesOnThisElf > maximumCaloriesPerElf) {
                maximumCaloriesPerElf = caloriesOnThisElf;
            }
        }
        return maximumCaloriesPerElf;
    }
}
