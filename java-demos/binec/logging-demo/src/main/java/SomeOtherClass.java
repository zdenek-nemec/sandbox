import java.util.logging.Logger;

public class SomeOtherClass {
    private final static Logger LOGGER = Logger.getLogger(SomeOtherClass.class.getName());

    public static void someMethod() {
        LOGGER.info("Logger Name: " + LOGGER.getName());
        LOGGER.info("This is info-level message in SomeOtherClass.someMethod().");
    }
}
