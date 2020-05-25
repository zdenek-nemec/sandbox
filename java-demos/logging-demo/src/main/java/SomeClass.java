import java.util.logging.Logger;

public class SomeClass {
    public static void someMethod() {
        Logger logger = Logger.getLogger(Logger.GLOBAL_LOGGER_NAME);
        logger.info("This is info-level message in SomeClass.someMethod().");
    }
}
