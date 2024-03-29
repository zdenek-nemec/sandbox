package cz.zdenek.sandbox;

import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.text.SimpleDateFormat;
import java.util.Date;

public class BlackMedJobTransfer extends BlackMedJob {
    private static final Object sync = new Object();
    private static final String MEASUREMENT = "BlackMedTransferJob";
    private static final int GRAFANA_FILE_PERIOD_SECONDS = 1;
    private static final String GRAFANA_FILE_LOCATION = ".";
    private static final String GRAFANA_FILENAME_PREFIX = "grafana_";
    private static final String GRAFANA_FILE_TIMESTAMP_FORMAT = "yyyy-MM-dd_HH-mm-ss";
    private static FileOutputStream grafanaFile;
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
        Date endTimestamp = new Date();
        Date startTimestamp = new Date(endTimestamp.getTime() - duration);
        writeMetrics(startTimestamp, endTimestamp, RandomGenerator.getInt(10000));
        return true;
    }

    private void writeMetrics(Date startTimestamp, Date endTimestamp, int size) {
        System.out.println("BlackMedJobTransfer.writeMetrics");
        int durationSeconds = (int) (endTimestamp.getTime() - startTimestamp.getTime()) / 1000 + 1;
        String metrics = String.format("%s,id=%d,name=%s,source=%s,destination=%s size=%d,duration=%d %s\n",
                MEASUREMENT,
                this.getId(),
                this.getName(),
                this.source,
                this.destination,
                size,
                durationSeconds,
                startTimestamp.getTime() + "000000"
        );
        System.out.println(metrics);
        synchronized (sync) {
            grafanaFile = getGrafanaFile();
            try {
                grafanaFile.write(metrics.getBytes());
            } catch (IOException e) {
                throw new RuntimeException(e);
            }
        }
    }

    private FileOutputStream getGrafanaFile() {
        if (grafanaFile == null) {
            SimpleDateFormat grafanaFilenameTimestamp = new SimpleDateFormat(GRAFANA_FILE_TIMESTAMP_FORMAT);
            String fileName = GRAFANA_FILENAME_PREFIX + grafanaFilenameTimestamp.format(new Date());
            try {
                grafanaFile = new FileOutputStream(GRAFANA_FILE_LOCATION + "/" + fileName + ".tmp", true);
            } catch (FileNotFoundException e) {
                throw new RuntimeException(e);
            }

            new Thread(() -> {
                try {
                    Thread.sleep(GRAFANA_FILE_PERIOD_SECONDS * 1000);
                } catch (InterruptedException e) {
                    throw new RuntimeException(e);
                }

                synchronized (sync) {
                    try {
                        System.out.println("bla");
                        grafanaFile.close();
                        Files.move(
                                Paths.get(GRAFANA_FILE_LOCATION + "/" + fileName + ".tmp"),
                                Paths.get(GRAFANA_FILE_LOCATION + "/" + fileName + ".log")
                        );
                        grafanaFile = null;
                    } catch (IOException e) {
                        throw new RuntimeException(e);
                    }
                }
            }).start();
        }
        return grafanaFile;
    }
}
