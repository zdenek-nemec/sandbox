import sun.rmi.runtime.Log;

import java.io.IOException;
import java.util.logging.*;

public class MainClass {
    private final static Logger LOGGER = Logger.getLogger(Logger.GLOBAL_LOGGER_NAME);

    public static void main(String[] args) throws IOException {
        System.setProperty("java.util.logging.SimpleFormatter.format", "%1$tF %1$tT [%4$-7s] %2$s(): %5$s %n");
        LOGGER.setLevel(Level.ALL);
        Logger.getLogger("").getHandlers()[0].setLevel(Level.ALL);

        Handler fileHandler = new FileHandler("./logging-demo.log");
        LOGGER.addHandler(fileHandler);
        fileHandler.setLevel(Level.ALL);

        LOGGER.info("Logger Name: " + LOGGER.getName());

        LOGGER.severe("This is severe-level message in MainClass.main().");
        LOGGER.warning("This is warning-level message in MainClass.main().");
        LOGGER.info("This is info-level message in MainClass.main().");
        LOGGER.config("This is config-level message in MainClass.main().");
        LOGGER.fine("This is fine-level message in MainClass.main().");
        LOGGER.finer("This is finer-level message in MainClass.main().");
        LOGGER.finest("This is finest-level message in MainClass.main().");

        otherMethod();

        SomeClass.someMethod();

        SomeOtherClass.someMethod();
    }

    private static void otherMethod() {
        LOGGER.info("This is info-level message in MainClass.otherMethod().");
    }
}
