package cz.zdenek.sandbox;

import java.util.Date;

public class BlackMedJob {
    private BlackMedMetrics metrics;

    public BlackMedJob() {
        System.out.println("BlackMedJob.constructor");
        this.metrics = null;
    }

    protected void generateMetrics(String type, Integer id, String name, String source, String destination, Integer size, Date startTime, Date endTime) {
        this.metrics = new BlackMedMetrics(type, id, name, source, destination, size, startTime, endTime);
    }

    private String getMetricsInfluxDbFormat() {
        StringBuilder stringBuilder = new StringBuilder();
        stringBuilder.append(metrics.getType() + " " + metrics.getName() + " " + metrics.getId());
        return stringBuilder.toString();
    }

    protected void writeMetrics() {
        System.out.println("BlackMedJob.writeMetrics");
        System.out.println(getMetricsInfluxDbFormat());
    }
}
