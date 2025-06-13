package org.zdenek
package languageselectorcomponent

import org.apache.wicket.markup.html.WebPage
import org.apache.wicket.markup.html.basic.Label
import org.apache.wicket.markup.html.form.DropDownChoice
import org.apache.wicket.markup.html.link.BookmarkablePageLink
import org.apache.wicket.model.PropertyModel

import java.util.Locale
import scala.jdk.CollectionConverters._

class LanguageSelectorComponentPage extends WebPage {
  private val supportedLocales = List(
    new Locale("en"),
    new Locale("cs"),
    new Locale("de"),
    new Locale("ru"),
  )

  var selectedLocale: Locale = getSession.getLocale

  override def onInitialize(): Unit = {
    super.onInitialize()

    val languageSelectorComponentPage = new DropDownChoice[Locale](
      "languageSelectorComponentPage",
      new PropertyModel[Locale](this, "selectedLocale"),
      supportedLocales.asJava,
      new org.apache.wicket.markup.html.form.IChoiceRenderer[Locale] {
        override def getDisplayValue(locale: Locale): String = locale.getDisplayLanguage(locale)
        override def getIdValue(locale: Locale, index: Int): String = locale.toLanguageTag
      }
    )

    languageSelectorComponentPage.add(new org.apache.wicket.ajax.form.AjaxFormComponentUpdatingBehavior("change") {
      override def onUpdate(target: org.apache.wicket.ajax.AjaxRequestTarget): Unit = {
        getSession.setLocale(selectedLocale)
        setResponsePage(classOf[LanguageSelectorComponentPage])
      }
    })
    add(languageSelectorComponentPage)

    add(new Label("selected-language", selectedLocale))

    add(new BookmarkablePageLink[Void]("toPage2", classOf[LanguageSelectorComponentPage2]))
  }
}
