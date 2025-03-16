package cz.zdenek.sandbox.demos
package codewars

object GetCharacterFromAsciiValue {
  def getChar(c: Int): Char = c.toChar

  def main(args: Array[String]): Unit = {
    println("Get character from ASCII Value")
    println(getChar(67))
  }
}
