package cz.zdenek.sandbox.adventofcode2022.day1;

import java.util.Hashtable;
import java.util.Iterator;
import java.util.List;

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
        Hashtable<Integer, Integer> caloriesPerElf = new Hashtable<>();
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
                caloriesPerElf.put(elves, caloriesPerElf.get(elves) + Integer.parseInt(line));
            }
        }
        return caloriesPerElf;
    }

    public Integer getMostCaloriesElfKey(Hashtable<Integer, Integer> caloriesPerElf) {
        Iterator<Integer> keys = caloriesPerElf.keySet().iterator();
        Integer maximumCaloriesKey = keys.next();
        Integer maximumCaloriesValue = caloriesPerElf.get(maximumCaloriesKey);
        while (keys.hasNext()) {
            Integer key = keys.next();
            Integer value = caloriesPerElf.get(key);
            if (value > maximumCaloriesValue) {
                maximumCaloriesKey = key;
                maximumCaloriesValue = value;
            }
        }
        return maximumCaloriesKey;
    }

    public Integer getMostCaloriesOnElf() {
        Hashtable<Integer, Integer> caloriesPerElf = getCaloriesPerElf();
        return caloriesPerElf.get(getMostCaloriesElfKey(caloriesPerElf));
    }

    public Integer getCaloriesOnTopXElves(int numberOfTopElves) {
        Hashtable<Integer, Integer> caloriesPerElf = getCaloriesPerElf();
        Integer calories = 0;
        for (int i = 0; i < numberOfTopElves; i++) {
            Integer topElfKey = getMostCaloriesElfKey(caloriesPerElf);
            calories += caloriesPerElf.get(topElfKey);
            caloriesPerElf.remove(topElfKey);
        }
        return calories;
    }
}
