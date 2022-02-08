import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

public class JavaSelenium {
    public static void main(String[] args) {
        WebDriver driver = new ChromeDriver();
        driver.get("https://selenium.dev");
        String title = driver.getTitle();
        System.out.println("The title is " + title);
        driver.quit();
    }
}
