package cz.zdenek.sandbox.demos
package codewars

// https://www.codewars.com/kata/559d2284b5bb6799e9000047/train/scala
object AddLength {
  def addLength(s: String): Seq[String] = {
    s.split(" ").toSeq.map(word => s"$word ${word.length}")
  }

  def main(args: Array[String]): Unit = {
    println("Add Length")
    println(addLength("apple ban"))
  }
}
