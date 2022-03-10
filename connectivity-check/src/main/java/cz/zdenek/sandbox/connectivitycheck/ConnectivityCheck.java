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
            target_list_file = "sftp_targets.txt";
        }

        List<String> target_list;
        try {
            target_list = Files.lines(Paths.get(target_list_file)).collect(Collectors.toList());
        } catch (FileNotFoundException e) {
            System.out.println("Cannot read input file");
            throw e;
        }

        System.out.println("Target,Connectivity Test");
        for (String target : target_list) {
            System.out.print(target + ":22,");
            try (Socket clientSocket = new Socket(target, 22)) {
                System.out.println("successful");
            } catch (Exception e) {
                System.out.println("failed");
            }
        }
    }
}
