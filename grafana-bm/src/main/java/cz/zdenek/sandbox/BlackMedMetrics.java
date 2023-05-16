package cz.zdenek.sandbox;

import java.util.Date;

public class BlackMedMetrics {
    private final String type;
    private final Integer id;
    private final String name;
    private final String source;
    private final String destination;
    private final Integer size;
    private final Date startTime;
    private final Date endTime;

    public BlackMedMetrics(String type, Integer id, String name, String source, String destination, Integer size, Date startTime, Date endTime) {
        this.type = type;
        this.id = id;
        this.name = name;
        this.source = source;
        this.destination = destination;
        this.size = size;
        this.startTime = startTime;
        this.endTime = endTime;
    }

    public String getType() {
        return type;
    }

    public Integer getId() {
        return id;
    }

    public String getName() {
        return this.name;
    }

    public String getSource() {
        return source;
    }

    public String getDestination() {
        return destination;
    }

    public Integer getSize() {
        return size;
    }

    public Date getStartTime() {
        return startTime;
    }

    public Date getEndTime() {
        return endTime;
    }
}
