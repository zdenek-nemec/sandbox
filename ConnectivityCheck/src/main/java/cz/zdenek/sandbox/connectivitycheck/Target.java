package cz.zdenek.sandbox.connectivitycheck;

import java.net.Socket;

public class Target {
    public static final String REPORT_HEADER = "#Target,Connection Test,Login Test,Description";
    public final String login;
    public final String host;
    public final int port;
    public final String description;
    private TestResult connectionTestPassed = TestResult.NOT_TESTED;

    Target(String line) {
        String[] targetInfo = line.split(",", 4);
        login = targetInfo[0];
        host = targetInfo[1];
        port = Integer.parseInt(targetInfo[2]);
        description = targetInfo[3];
    }

    public void testConnectivity() {
        testConnection();
//        testLogin();
    }

    public void testConnection() {
        try (Socket clientSocket = new Socket(host, port)) {
            connectionTestPassed = TestResult.SUCCESSFUL;
        } catch (Exception e) {
            connectionTestPassed = TestResult.FAILED;
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
        return connectionTestPassed.description;
    }

    private String getLoginTestResult() {
        return TestResult.NOT_TESTED.description;
    }

    public enum TestResult {
        NOT_TESTED("-"),
        SUCCESSFUL("successful"),
        FAILED("failed");

        public final String description;

        TestResult(String description) {
            this.description = description;
        }
    }
}
