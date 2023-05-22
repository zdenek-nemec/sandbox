package cz.zdenek.sandbox;

import java.io.IOException;

public class Main {
    private static final int JOBS_COUNT = 3;
    private static final int WAIT_PERIOD = 500;

    public static void main(String[] args) throws InterruptedException, IOException {
        System.out.println("Grafana BM");

        for (int i = 0; i < JOBS_COUNT; i++) {
            System.out.println("Running job " + i);
            if (i % 2 == 0) {
                System.out.println("Transfer job");
                BlackMedJobTransfer blackMedJobTransfer = new BlackMedJobTransfer(
                        i,
                        RandomGenerator.getString(10),
                        RandomGenerator.getString(20),
                        RandomGenerator.getString(20)
                );
                if (!blackMedJobTransfer.run()) {
                    System.out.println("Transfer job error");
                }
            } else {
                System.out.println("Shell job");
                BlackMedJobShell blackMedJobShell = new BlackMedJobShell(i, RandomGenerator.getString(10));
                if (!blackMedJobShell.run()) {
                    System.out.println("Shell job error");
                }
            }
            Thread.sleep(WAIT_PERIOD);
            System.out.println();
        }
    }
}
