package cz.zdenek.sandbox;

public class Main {
    public static void main(String[] args) {
        System.out.println("Hello, World!");

        System.out.println("Transfer job");
        BlackMedJobTransfer blackMedJobTransfer = new BlackMedJobTransfer();
        if (!blackMedJobTransfer.run()) {
            System.out.println("Transfer job error");
        }
        System.out.println();

        System.out.println("Shell job");
        BlackMedJobShell blackMedJobShell = new BlackMedJobShell();
        if (!blackMedJobShell.run()) {
            System.out.println("Shell job error");
        }
        System.out.println();
    }
}
