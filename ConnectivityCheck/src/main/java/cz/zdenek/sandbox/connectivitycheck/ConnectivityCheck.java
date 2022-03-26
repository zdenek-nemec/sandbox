package cz.zdenek.sandbox.connectivitycheck;

import java.io.IOException;
import java.net.Socket;
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
        List<Target> targets = getTargets(args);

        System.out.println("#Target,Connectivity Test,Login Test,Description");
        for (Target target : targets) {
            if (target.login.equals("")) {
                System.out.print(target.host + ":" + target.port + ",");
            } else {
                System.out.print(target.login + "@" + target.host + ":" + target.port + ",");
            }
            try (Socket clientSocket = new Socket(target.host, target.port)) {
                System.out.print("successful,-,");
            } catch (Exception e) {
                System.out.print("failed,-,");
            }
            System.out.println(target.description);
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
            System.out.println("Cannot read input file");
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
