package org.zdenek
package basicelements

import org.apache.wicket.markup.html.WebPage
import org.apache.wicket.markup.html.basic.Label
import org.apache.wicket.markup.html.form.{DropDownChoice, TextField}
import org.apache.wicket.model.Model

import java.util

class BasicElements extends WebPage {
  add(new Label("message", "Hello, Basic Elements!"))

  add(new Label("heading", "Wicket Scala Heading"))

  add(new Label("paragraph", "This is a paragraph from Scala code."))

  add(new TextField[String]("inputField", Model.of("")))

  val options = util.Arrays.asList("Option 1", "Option 2", "Option 3")
  add(new DropDownChoice[String]("dropdown", Model.of("Option 1"), options))
}
