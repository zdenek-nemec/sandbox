package cz.zdenek.sandbox;

import java.util.Date;

public class BlackMedJobShell extends BlackMedJob {
    public BlackMedJobShell() {
        System.out.println("BlackMedJobShell.constructor");
    }

    private void generateMetrics() {
        this.generateMetrics(
                "ShellJob",
                0,
                RandomStringGenerator.generateRandomString(10),
                RandomStringGenerator.generateRandomString(10),
                RandomStringGenerator.generateRandomString(10),
                0,
                new Date(),
                new Date()
        );
    }

    public boolean run() {
        System.out.println("BlackMedJobShell.run");
        this.generateMetrics();
        this.writeMetrics();
        return true;
    }
}
