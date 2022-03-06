import java.io.IOException;
import java.net.Socket;

public class ConnectivityCheck {
    public static void main(String[] args) throws IOException {
        System.out.println("Hello, Connectivity Check!");

        String[] target_list = {"avl4658t", "localhost"};

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
