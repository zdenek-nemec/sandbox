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
        new ConnectivityCheck().runCheck();
    }

    private void runCheck() throws IOException {
        System.out.println("Hello, Connectivity Check!");

        List<String> target_list;
        try {
            target_list = Files.lines(Paths.get("sftp_targets.txt")).collect(Collectors.toList());
        } catch (FileNotFoundException e) {
            System.out.println("Cannot read input file");
            throw e;
        }

        System.out.println("Target,Connectivity Test");
        for (String target : target_list) {
            System.out.print(target + ":22,");
            try (Socket clientSocket = new Socket(target, 22)) {
                System.out.println("success");
            } catch (Exception e) {
                System.out.println("failed");
            }
        }
    }
}
