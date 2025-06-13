package org.zdenek
package languageselectorcomponent.languageselector

import org.apache.wicket.markup.html.WebPage
import org.apache.wicket.markup.html.basic.Label
import org.apache.wicket.markup.html.form.DropDownChoice
import org.apache.wicket.markup.html.panel.Panel
import org.apache.wicket.model.PropertyModel
import org.zdenek.languageselectorcomponent.LanguageSelectorComponentPage

import java.util.Locale
import scala.jdk.CollectionConverters.SeqHasAsJava

class LanguageSelectorComponent(id: String, pageClass: Class[_ <: WebPage]) extends Panel(id) {
  private val supportedLocales = List(
    new Locale("en"),
    new Locale("cs"),
    new Locale("de"),
    new Locale("ru"),
  )

  var selectedLocale: Locale = getSession.getLocale

  override def onInitialize(): Unit = {
    super.onInitialize()

    val languageSelectorComponent = new DropDownChoice[Locale](
      "languageSelectorComponentDropdown",
      new PropertyModel[Locale](this, "selectedLocale"),
      supportedLocales.asJava,
      new org.apache.wicket.markup.html.form.IChoiceRenderer[Locale] {
        override def getDisplayValue(locale: Locale): String = locale.getDisplayLanguage(locale)
        override def getIdValue(locale: Locale, index: Int): String = locale.toLanguageTag
      }
    )

    languageSelectorComponent.add(new org.apache.wicket.ajax.form.AjaxFormComponentUpdatingBehavior("change") {
      override def onUpdate(target: org.apache.wicket.ajax.AjaxRequestTarget): Unit = {
        getSession.setLocale(selectedLocale)
        setResponsePage(pageClass)
      }
    })
    add(languageSelectorComponent)

    add(new Label("selected-language", selectedLocale))
  }
}
