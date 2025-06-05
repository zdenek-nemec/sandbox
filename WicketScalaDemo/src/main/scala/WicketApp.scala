package org.zdenek

import org.apache.wicket.markup.html.WebPage
import org.apache.wicket.protocol.http.WebApplication

class WicketApp extends WebApplication {
  override def getHomePage: Class[_ <: WebPage] = classOf[HelloWorldPage]
}
