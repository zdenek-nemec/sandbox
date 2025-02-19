package cz.zdenek.sandbox.demos
package codewars

object RoundToTheNextMultipleOf5 {
  def main(args: Array[String]): Unit = {
    println("Round up to the next multiple of 5")

    println(roundToNext5(12) + " 15")
    println(roundToNext5(15) + " 15")
    println(roundToNext5(-7) + " -5")
    println(roundToNext5(-1) + " 0")

    println(roundToNext5(0) + " 0")
    println(roundToNext5(2) + " 5")
    println(roundToNext5(3) + " 5")
    println(roundToNext5(12) + " 15")
    println(roundToNext5(21) + " 25")
    println(roundToNext5(-2) + " 0")
    println(roundToNext5(-5) + " -5")
  }

  private def roundToNext5(number: Int): Int = {
    val rem = number % 5
    if (rem == 0) {
      number;
    } else if (rem > 0) {
      number + (5 - rem);
    } else {
      number - rem;
    }
  }
}
