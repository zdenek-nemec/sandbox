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
        writeMetrics(RandomGenerator.getInt(1000), new Date(), new Date());
        return true;
    }

    private void writeMetrics(int size, Date startTimestamp, Date endTimestamp) {
        System.out.println("BlackMedJobTransfer.writeMetrics");
        String metrics = String.format("%s,%d,%s,%s,%s %d,%s,%s",
                this.getType(),
                this.getId(),
                this.getName(),
                this.source,
                this.destination,
                size,
                startTimestamp.getTime() + "000000",
                endTimestamp.getTime() + "000000"
        );
        System.out.println(metrics);
    }
}
