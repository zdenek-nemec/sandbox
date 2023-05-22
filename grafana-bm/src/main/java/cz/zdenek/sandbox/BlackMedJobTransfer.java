package cz.zdenek.sandbox;

import java.util.Date;

public class BlackMedJobTransfer extends BlackMedJob {
    public BlackMedJobTransfer() {
        System.out.println("BlackMedJobTransfer.constructor");
    }

    private void generateMetrics() {
        this.generateMetrics(
                "TransferJob",
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
        System.out.println("BlackMedJobTransfer.run");
        this.generateMetrics();
        this.writeMetrics();
        return true;
    }
}
