package cz.zdenek.sandbox;

public class Main {
    public static void main(String[] args) {
        System.out.println("Hello, World!");

        BlackMedMock blackMed = new BlackMedMock();
        System.out.println(blackMed.getMetric().getType()
                + " "
                + blackMed.getMetric().getId().toString()
                + " "
                + blackMed.getMetric().getName()
        );
    }
}
