import java.util.logging.Level;
import java.util.logging.Logger;

public class MainClass {
    public static void main(String[] args) {
        Logger logger = Logger.getLogger(Logger.GLOBAL_LOGGER_NAME);
        logger.setLevel(Level.INFO);
        logger.severe("This is severe-level message.");
        logger.warning("This is warning-level message.");
        logger.info("This is info-level message.");
        logger.config("This is config-level message.");
        logger.fine("This is fine-level message.");
        logger.finer("This is finer-level message.");
        logger.finest("This is finest-level message.");
    }
}
