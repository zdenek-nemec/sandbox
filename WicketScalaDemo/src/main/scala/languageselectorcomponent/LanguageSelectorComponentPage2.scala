package org.zdenek
package languageselectorcomponent

import languageselectorcomponent.languageselector.LanguageSelectorComponent

import org.apache.wicket.markup.html.WebPage

class LanguageSelectorComponentPage2 extends WebPage {

  override def onInitialize(): Unit = {
    super.onInitialize()
    add(new LanguageSelectorComponent("languageSelectorComponent", classOf[LanguageSelectorComponentPage2]))
  }
}
