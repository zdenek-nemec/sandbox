package cz.zdenek.sandbox;

import java.util.Date;

public class BlackMedMock {
    public static void main(String[] args) {
        System.out.println("BlackMed.main");
    }

    public BlackMedMetrics getMetric() {
        return new BlackMedMetrics(
                RandomStringGenerator.generateRandomString(1),
                0,
                RandomStringGenerator.generateRandomString(10),
                RandomStringGenerator.generateRandomString(10),
                RandomStringGenerator.generateRandomString(10),
                0,
                new Date(),
                new Date()
        );
    }
}
