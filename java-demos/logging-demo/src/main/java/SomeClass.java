import java.util.logging.Logger;

public class SomeClass {
    private final static Logger LOGGER = Logger.getLogger(Logger.GLOBAL_LOGGER_NAME);

    public static void someMethod() {
        LOGGER.info("Logger Name: " + LOGGER.getName());
        LOGGER.info("This is info-level message in SomeClass.someMethod().");
    }
}
