package cz.zdenek.sandbox.demos
package codewars

import org.junit.jupiter.api.Assertions.assertEquals
import org.junit.jupiter.api.Test

class AddLengthTest {
  @Test
  def testAddLength(): Unit = {
    val testCases = Seq(
      ("apple ban", Seq("apple 5", "ban 3")),
      ("you will win", Seq("you 3", "will 4", "win 3")),
      ("you", Seq("you 3")),
      ("y", Seq("y 1")),
      ("x y z", Seq("x 1", "y 1", "z 1")),
      ("xyz", Seq("xyz 3")),
      ("xyz x y z xyz", Seq("xyz 3", "x 1", "y 1", "z 1", "xyz 3")),
      ("a bc cde", Seq("a 1", "bc 2", "cde 3")),
      ("a ab abc", Seq("a 1", "ab 2", "abc 3")),
      ("a ab abc ab a", Seq("a 1", "ab 2", "abc 3", "ab 2", "a 1"))
    )

    for (testCase <- testCases) {
      assertEquals(testCase._2, AddLength.addLength(testCase._1))
    }
  }
}
