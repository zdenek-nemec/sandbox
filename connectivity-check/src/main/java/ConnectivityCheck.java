import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.net.Socket;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class ConnectivityCheck {
    public static void main(String[] args) throws IOException {
        System.out.println("Hello, Connectivity Check!");

        List<String> target_list = new ArrayList<>();
        try {
            File file = new File("sftp_targets.txt");
            Scanner scanner = new Scanner(file);
            while (scanner.hasNextLine()) {
                String line = scanner.nextLine();
                target_list.add(line);
            }
            scanner.close();
        } catch (FileNotFoundException e) {
            System.out.println("Cannot read input file");
            e.printStackTrace();
        }

        System.out.println("Target,Connectivity Test");
        for (String target : target_list) {
            System.out.print(target + ":22,");
            try {
                Socket clientSocket = new Socket(target, 22);
                System.out.println("success");
            } catch (Exception e) {
                System.out.println("failed");
            }
        }
    }
}
