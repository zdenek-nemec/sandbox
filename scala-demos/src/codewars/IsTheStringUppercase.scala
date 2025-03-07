package cz.zdenek.sandbox.demos
package codewars

// https://www.codewars.com/kata/56cd44e1aa4ac7879200010b/train/scala
object IsTheStringUppercase {
  def isUpperCase(inp: String): Boolean = {
    for (c <- inp) {
      if (c.isLower) {
        return false
      }
    }
    true
  }

  def isUpperCase2(s: String): Boolean = s.forall(!_.isLower)

  def main(args: Array[String]): Unit = {
    println("Is the string uppercase?")
    println(isUpperCase("Ahoj"))
    println(isUpperCase("AHOJ"))
    println(isUpperCase2("Ahoj"))
    println(isUpperCase2("AHOJ"))
  }
}
