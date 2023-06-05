package cz.zdenek.sandbox;

public class BlackMedJobShell extends BlackMedJob {
    public BlackMedJobShell(int id, String name) {
        super("ShellJob", id, name);
        System.out.println("BlackMedJobShell.constructor");
    }

    public boolean run() {
        System.out.println("BlackMedJobShell.run");
        return true;
    }
}
