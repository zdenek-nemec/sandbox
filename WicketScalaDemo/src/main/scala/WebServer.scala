package org.zdenek

import org.apache.wicket.protocol.http.WicketFilter
import org.eclipse.jetty.server.Server
//import org.eclipse.jetty.servlet.{ServletContextHandler, ServletHolder}
import org.eclipse.jetty.servlet.{ServletContextHandler, FilterHolder}

object WebServer extends App {
  val server = new Server(8080)
  val context = new ServletContextHandler(ServletContextHandler.SESSIONS)
  context.setContextPath("/")
//  val filter = new ServletHolder(classOf[WicketFilter])
//  filter.setInitParameter("applicationClassName", "your.package.WicketApp")
//  filter.setInitParameter(WicketFilter.FILTER_MAPPING_PARAM, "/*")
//  context.addFilter(classOf[WicketFilter], "/*", null)

  val filter = new FilterHolder(new WicketFilter())
  filter.setInitParameter("applicationClassName", "org.zdenek.WicketApp")
  filter.setInitParameter(WicketFilter.FILTER_MAPPING_PARAM, "/*")
  context.addFilter(filter, "/*", null)

  server.setHandler(context)
  server.start()
  server.join()
}
