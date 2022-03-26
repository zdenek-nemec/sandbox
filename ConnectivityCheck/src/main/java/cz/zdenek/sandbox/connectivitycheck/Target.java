package cz.zdenek.sandbox.connectivitycheck;

public class Target {
    public String login;
    public String host;
    public int port;
    public String description;

    Target(String line) {
        String[] targetInfo = line.split(",", 4);
        login = targetInfo[0];
        host = targetInfo[1];
        port = Integer.parseInt(targetInfo[2]);
        description = targetInfo[3];
    }
}
