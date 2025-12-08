package org.zdenek
package ajaxcomponent

import org.apache.wicket.ajax.AjaxRequestTarget
import org.apache.wicket.ajax.form.OnChangeAjaxBehavior
import org.apache.wicket.markup.html.WebPage
import org.apache.wicket.markup.html.form.TextField
import org.apache.wicket.model.Model

case class UserData(name: String, description: String)

class AjaxComponent extends WebPage {
  val userModel = Model.of(UserData("", ""))
  val nameField = new TextField[String]("myDescriptionField", userModel.map(_.name))
  val descriptionField = new TextField[String]("myNameField", userModel.map(_.description))

//  Cannot compile because of type
  nameField.add(new OnChangeAjaxBehavior {
      override def onUpdate(target: AjaxRequestTarget): Unit = {
        descriptionField.getDefaultModel.setObject(nameField.getModel.getObject)
        target.add(descriptionField)
      }
    })

  add(descriptionField)
  add(nameField)
}
