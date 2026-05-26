package cz.zdenek.sandbox.demos
package codewars

object BinToDecimal {
  def binToDec(bin: String): Int = Integer.parseInt(bin, 2)

  def main(args: Array[String]): Unit = {
    println("Bin to Decimal")
    println(s"${binToDec("10")}")
    println(s"${binToDec("111")}")
  }
}
