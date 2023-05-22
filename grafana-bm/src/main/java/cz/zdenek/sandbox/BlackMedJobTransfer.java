package cz.zdenek.sandbox;

import java.util.Date;

public class BlackMedJobTransfer extends BlackMedJob {
    private final String source;
    private final String destination;

    public BlackMedJobTransfer(int id, String name, String source, String destination) {
        super("TransferJob", id, name);
        System.out.println("BlackMedJobTransfer.constructor");
        this.source = source;
        this.destination = destination;
    }

    public boolean run() {
        System.out.println("BlackMedJobTransfer.run");
        int duration = RandomGenerator.getInt(100000);
        Date startTimestamp = new Date();
        Date endTimestamp = new Date(startTimestamp.getTime() + duration);
        writeMetrics(startTimestamp, endTimestamp, RandomGenerator.getInt(10000));
        return true;
    }

    private void writeMetrics(Date startTimestamp, Date endTimestamp, int size) {
        System.out.println("BlackMedJobTransfer.writeMetrics");
        int durationSeconds = (int) (endTimestamp.getTime() - startTimestamp.getTime()) / 1000 + 1;
        String metrics = String.format("BlackMedTransferJob,id=%d,name=%s,source=%s,destination=%s size=%d,duration=%d %s",
                this.getId(),
                this.getName(),
                this.source,
                this.destination,
                size,
                durationSeconds,
                startTimestamp.getTime() + "000000"
        );
        System.out.println(metrics);
    }
}
