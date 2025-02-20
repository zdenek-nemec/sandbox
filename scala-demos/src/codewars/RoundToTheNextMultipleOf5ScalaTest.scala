package cz.zdenek.sandbox.demos
package codewars

import org.junit.jupiter.api.Assertions.assertEquals
import org.junit.jupiter.api.Test

class RoundToTheNextMultipleOf5ScalaTest {
  @Test
  def testRoundToNext5Zero(): Unit = {
    assertEquals("Result should be 0", RoundToTheNextMultipleOf5.roundToNext5(0))
  }
}
