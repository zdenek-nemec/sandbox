import java.util.logging.Level;
import java.util.logging.Logger;

public class MainClass {
    private final static Logger logger = Logger.getLogger(Logger.GLOBAL_LOGGER_NAME);

    public static void main(String[] args) {
        logger.setLevel(Level.INFO);
        logger.severe("This is severe-level message in MainClass.main().");
        logger.warning("This is warning-level message in MainClass.main().");
        logger.info("This is info-level message in MainClass.main().");
        logger.config("This is config-level message in MainClass.main().");
        logger.fine("This is fine-level message in MainClass.main().");
        logger.finer("This is finer-level message in MainClass.main().");
        logger.finest("This is finest-level message in MainClass.main().");

        otherMethod();

        OtherClass.someMethod();
    }

    private static void otherMethod() {
        logger.info("This is info-level message in MainClass.otherMethod().");
    }
}
