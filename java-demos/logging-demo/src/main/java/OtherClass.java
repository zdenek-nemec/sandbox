import java.util.logging.Logger;

public class OtherClass {
    public static void someMethod() {
        Logger logger = Logger.getLogger(Logger.GLOBAL_LOGGER_NAME);
        logger.info("This is info-level message in OtherClass.someMethod().");
    }
}
