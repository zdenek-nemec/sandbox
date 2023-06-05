package cz.zdenek.sandbox.chatgpt;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

class Report {
    private Map<String, Integer> data;

    public Report() {
        data = new HashMap<>();
    }

    public void add(String key, int duration) {
        if (data.containsKey(key)) {
            int currentDuration = data.get(key);
            data.put(key, currentDuration + duration);
        } else {
            data.put(key, duration);
        }
    }

    public int size() {
        return data.size();
    }

    public void save(String path, String keyColumn) throws IOException {
        try (BufferedWriter writer = new BufferedWriter(new FileWriter(path))) {
            writer.write(keyColumn + ",Full-Path,Duration,Duration Converted");
            writer.newLine();
            for (Map.Entry<String, Integer> entry : data.entrySet()) {
                String[] keyParts = entry.getKey().split(",");
                String coreKey = keyParts[0];
                String fullPath = keyParts[1];
                int duration = entry.getValue();
                int hours = duration / (60 * 60);
                int minutes = (duration % (60 * 60)) / 60;
                int seconds = duration % 60;
                if (duration != hours * 60 * 60 + minutes * 60 + seconds) {
                    throw new RuntimeException("Duration mismatch");
                }
                String durationConverted = String.format("%d:%02d:%02d", hours, minutes, seconds);
                writer.write(String.format("%s,%s,%d,%s", coreKey, fullPath, duration, durationConverted));
                writer.newLine();
            }
        }
    }
}
