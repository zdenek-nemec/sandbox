package org.zdenek
package languageselector

import org.apache.wicket.markup.html.WebPage
import org.apache.wicket.markup.html.basic.Label
import org.apache.wicket.markup.html.form.DropDownChoice
import org.apache.wicket.model.PropertyModel

import java.util.Locale
import scala.collection.convert.ImplicitConversions.`collection asJava`
import scala.jdk.CollectionConverters._

class LanguageSelector extends WebPage {
  private val supportedLocales = List(
    new Locale("EN"),
    new Locale("CS"),
    new Locale("DE"),
    new Locale("ru"),
  )

  var selectedLocale: Locale = getSession.getLocale

  override def onInitialize(): Unit = {
    super.onInitialize()

    val languageSelector = new DropDownChoice[Locale](
      "languageSelector",
      new PropertyModel[Locale](this, "selectedLocale"),
      supportedLocales.asJava,
      new org.apache.wicket.markup.html.form.IChoiceRenderer[Locale] {
        override def getDisplayValue(locale: Locale): String = locale.getDisplayLanguage(locale)
        override def getIdValue(locale: Locale, index: Int): String = locale.toLanguageTag
      }
    )

    languageSelector.add(new org.apache.wicket.ajax.form.AjaxFormComponentUpdatingBehavior("change") {
      override def onUpdate(target: org.apache.wicket.ajax.AjaxRequestTarget): Unit = {
        getSession.setLocale(selectedLocale)
        setResponsePage(classOf[LanguageSelector])
      }
    })
    add(languageSelector)

    add(new Label("selected-language", selectedLocale))

    add(new Label("paragraph", new org.apache.wicket.model.StringResourceModel("info-p1", this)))
//    add(new Label("paragraph", new org.apache.wicket.model.Model[String] {
//      override def getObject: String = getSession.getLocale.getDisplayLanguage(getSession.getLocale)
//    }))
  }
}
