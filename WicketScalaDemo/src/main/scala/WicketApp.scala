package org.zdenek

import org.apache.wicket.markup.html.WebPage
import org.apache.wicket.protocol.http.WebApplication
import org.zdenek.basicelements.BasicElements
import org.zdenek.languageselector.LanguageSelector
import org.zdenek.languageselectorcomponent.LanguageSelectorComponentPage

class WicketApp extends WebApplication {
//  override def getHomePage: Class[_ <: WebPage] = classOf[HelloWorldPage]
//  override def getHomePage: Class[_ <: WebPage] = classOf[BasicElements]
//  override def getHomePage: Class[_ <: WebPage] = classOf[LanguageSelector]
  override def getHomePage: Class[_ <: WebPage] = classOf[LanguageSelectorComponentPage]
}
