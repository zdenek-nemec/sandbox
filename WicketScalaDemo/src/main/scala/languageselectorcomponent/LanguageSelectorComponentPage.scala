package org.zdenek
package languageselectorcomponent

import languageselectorcomponent.languageselector.LanguageSelectorComponent

import org.apache.wicket.markup.html.WebPage
import org.apache.wicket.markup.html.link.BookmarkablePageLink

class LanguageSelectorComponentPage extends WebPage {

  override def onInitialize(): Unit = {
    super.onInitialize()
    add(new LanguageSelectorComponent("languageSelectorComponent", classOf[LanguageSelectorComponentPage]))
    add(new BookmarkablePageLink[Void]("toPage2", classOf[LanguageSelectorComponentPage2])
    )
  }
}
