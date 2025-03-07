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


class Point {
  private var _x = 0
  private var _y = 0
  private val bound = 100

  def x: Int = _x
  def x_=(newValue: Int): Unit = {
    if (newValue < bound)
      _x = newValue
    else
      printWarning()
  }

  def y: Int = _y
  def y_=(newValue: Int): Unit = {
    if (newValue < bound)
      _y = newValue
    else
      printWarning()
  }

  private def printWarning(): Unit =
    println("WARNING: Out of bounds")
}

val point1 = new Point
point1.x = 99
point1.y = 101 // prints the warning