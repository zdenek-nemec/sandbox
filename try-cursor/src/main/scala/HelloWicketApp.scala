package example

import org.apache.wicket.protocol.http.WebApplication
import org.apache.wicket.markup.html.WebPage
import org.apache.wicket.markup.html.basic.Label
import org.apache.wicket.protocol.http.WicketServlet
import org.eclipse.jetty.server.Server
import org.eclipse.jetty.servlet.{ServletContextHandler, ServletHolder}

class HelloPage extends WebPage {
  add(new Label("message", "Hello, Wicket with Scala!"))
}

class HelloWicketApp extends WebApplication {
  override def getHomePage: Class[_ <: WebPage] = classOf[HelloPage]
}

object HelloWicketLauncher {
  def main(args: Array[String]): Unit = {
    val server = new Server(8080)
    val context = new ServletContextHandler(ServletContextHandler.SESSIONS)
    context.setContextPath("/")

    val holder = new ServletHolder(new WicketServlet())
    holder.setInitParameter("applicationClassName", classOf[HelloWicketApp].getName)
    holder.setInitParameter("filterMappingUrlPattern", "/*") // Required for Wicket
    context.addServlet(holder, "/*")

    server.setHandler(context)
    server.start()
    server.join()
  }
} 