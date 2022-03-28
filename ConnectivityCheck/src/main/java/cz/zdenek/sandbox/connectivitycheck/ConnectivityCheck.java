package cz.zdenek.sandbox.connectivitycheck;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

public class ConnectivityCheck {
    private static final boolean DEBUG = false; // TODO: Is this an idiotic idea? Using build configuration is probably better idea.

    public static void main(String[] args) throws IOException {
        if (DEBUG) {
            new ConnectivityCheck().runConnectivityCheck(new String[]{"targets.csv"});
        } else {
            new ConnectivityCheck().runConnectivityCheck(args);
        }
    }

    private void runConnectivityCheck(String[] args) throws IOException {
        List<Target> targets = getTargets(args); // TODO: Wouldn't be better to have variable name targetList?

        System.out.println(targets.get(0).getTestReportHeader());
        for (Target target : targets) {
            target.testConnectivity();
            System.out.println(target.getTestReport());
        }
    }

    private List<Target> getTargets(String[] args) throws IOException {
        String targetsFile = getTargetsFile(args);
        List<String> lines = getLines(targetsFile);
        return getTargetEntries(lines);
    }

    private String getTargetsFile(String[] args) {
        return args[0];
    }

    private List<String> getLines(String filename) throws IOException {
        try {
            return Files.lines(Paths.get(filename)).collect(Collectors.toList());
        } catch (IOException e) {
            System.out.println("Cannot read the input file");
            throw e;
        }
    }

    private List<Target> getTargetEntries(List<String> lines) {
        List<Target> targets = new ArrayList<>();
        for (String line : lines) {
            if (line.startsWith("#")) {
                continue;
            }
            targets.add(new Target(line));
        }
        return targets;
    }
}
