package cz.zdenek.sandbox.connectivitycheck;

import java.io.FileNotFoundException;
import java.io.IOException;
import java.net.Socket;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

public class ConnectivityCheck {
    public static void main(String[] args) throws IOException {
        new ConnectivityCheck().runConnectivityCheck(args);
    }

    private void runConnectivityCheck(String[] args) throws IOException {
        String target_list_file;
        if (args.length == 1) {
            target_list_file = args[0];
        } else {
            target_list_file = "targets.csv";
        }

        List<String> lines;
        try {
            lines = Files.lines(Paths.get(target_list_file)).collect(Collectors.toList());
        } catch (FileNotFoundException e) {
            System.out.println("Cannot read input file");
            throw e;
        }

        List<Target> targets = new ArrayList<>();
        for (String line : lines) {
            if (line.startsWith("#")) {
                continue;
            }
            targets.add(new Target(line));
        }

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
}
