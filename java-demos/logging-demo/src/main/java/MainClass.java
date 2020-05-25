import java.util.logging.Level;
import java.util.logging.Logger;

public class MainClass {
    private final static Logger LOGGER = Logger.getLogger(Logger.GLOBAL_LOGGER_NAME);

    public static void main(String[] args) {
        LOGGER.setLevel(Level.ALL);

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
    }

    private static void otherMethod() {
        LOGGER.info("This is info-level message in MainClass.otherMethod().");
    }
}
