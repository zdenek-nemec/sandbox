package cz.zdenek.sandbox.demos
package codewars

import org.junit.jupiter.api.Assertions.assertEquals
import org.junit.jupiter.api.Test

class IsTheStringUppercaseTest {
  @Test
  def testIsUpperCase(): Unit = {
    assertEquals(false, IsTheStringUppercase.isUpperCase("Ahoj"))
    assertEquals(true, IsTheStringUppercase.isUpperCase("AHOJ"))
  }

  @Test
  def testIsUpperCase2(): Unit = {
    assertEquals(false, IsTheStringUppercase.isUpperCase2("Ahoj"))
    assertEquals(true, IsTheStringUppercase.isUpperCase2("AHOJ"))
  }
}
