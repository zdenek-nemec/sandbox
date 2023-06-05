package cz.zdenek.sandbox;

public class BlackMedJob {
    private final String type;
    private final int id;
    private final String name;

    public BlackMedJob(String type, int id, String name) {
        System.out.println("BlackMedJob.constructor");
        this.type = type;
        this.id = id;
        this.name = name;
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
}
