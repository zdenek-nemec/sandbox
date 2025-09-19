package org.zdenek
package ajaxcomponent

import org.apache.wicket.markup.html.WebPage
import org.apache.wicket.markup.html.basic.Label
import org.apache.wicket.markup.html.form.TextField
import org.apache.wicket.model.Model

class AjaxComponent extends WebPage{
  add(new TextField[String]("myInputField", Model.of("")))
  add(new Label("myParagraph", "This is a paragraph from Scala code."))
}
