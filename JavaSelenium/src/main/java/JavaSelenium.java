import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

public class JavaSelenium {
    public static void main(String[] args) {
        WebDriver webDriver = new ChromeDriver();
        webDriver.get("https://selenium.dev");
        String title = webDriver.getTitle();
        System.out.println("The title of the page is " + title);
        webDriver.quit();
    }
}
