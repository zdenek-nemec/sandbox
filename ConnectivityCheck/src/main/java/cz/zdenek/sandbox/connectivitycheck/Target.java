package cz.zdenek.sandbox.connectivitycheck;

import java.net.Socket;

public class Target {
    public String login;
    public String host;
    public int port;
    public String description;
    private boolean connectionTestPassed = false;

    Target(String line) {
        String[] targetInfo = line.split(",", 4);
        login = targetInfo[0];
        host = targetInfo[1];
        port = Integer.parseInt(targetInfo[2]);
        description = targetInfo[3];
    }

    public String getTestReportHeader() {
        return "#Target,Connection Test,Login Test,Description";
    }

    public void testConnectivity() {
        testConnection();
//        testLogin();
    }

    public void testConnection() {
        try (Socket clientSocket = new Socket(host, port)) {
            connectionTestPassed = true;
        } catch (Exception e) {
            connectionTestPassed = false; // TODO: Is this necessary? Can I store null to boolean?
        }
    }

    public String getTestReport() {
        if (login.equals("")) {
            return host + ":" + port + "," + getConnectionTestResult() + "," + getLoginTestResult() + "," + description;
        } else {
            return login + "@" + host + ":" + port + "," + getConnectionTestResult() + "," + getLoginTestResult() + "," + description;
        }
    }

    private String getConnectionTestResult() {
        return getTestResult(connectionTestPassed);
    }

    private String getLoginTestResult() {
        return "-";
    }

    private String getTestResult(boolean result) {
        if (result) {
            return "successful";
        } else {
            return "failed";
        }
    }
}
