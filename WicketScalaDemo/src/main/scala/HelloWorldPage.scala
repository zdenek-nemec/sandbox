package org.zdenek

import org.apache.wicket.markup.html.WebPage
import org.apache.wicket.markup.html.basic.Label

class HelloWorldPage extends WebPage {
  add(new Label("message", "Hello, World from Scala and Wicket!"))
}
