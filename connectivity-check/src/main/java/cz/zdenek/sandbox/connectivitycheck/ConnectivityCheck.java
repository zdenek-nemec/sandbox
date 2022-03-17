package cz.zdenek.sandbox.connectivitycheck;

import java.io.FileNotFoundException;
import java.io.IOException;
import java.net.Socket;
import java.nio.file.Files;
import java.nio.file.Paths;
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

        List<String> target_list;
        try {
            target_list = Files.lines(Paths.get(target_list_file)).collect(Collectors.toList());
        } catch (FileNotFoundException e) {
            System.out.println("Cannot read input file");
            throw e;
        }

        System.out.println("#Target,Connectivity Test,Login Test");
        for (String target : target_list) {
            if (target.startsWith("#User")) {
                continue;
            }
            String[] targetInfo = target.split(",");
            String login = targetInfo[0];
            String host = targetInfo[1];
            int port = Integer.parseInt(targetInfo[2]);
            if (targetInfo[0].equals("")) {
                System.out.print(host + ":" + port + ",");
            } else {
                System.out.print(login + "@" + host + ":" + port + ",");
            }
            try (Socket clientSocket = new Socket(host, port)) {
                System.out.println("successful,-");
            } catch (Exception e) {
                System.out.println("failed,-");
            }
        }
    }
}
