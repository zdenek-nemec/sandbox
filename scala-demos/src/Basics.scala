package cz.zdenek.sandbox.demos

// https://docs.scala-lang.org/tour/basics.html

object Basics {
  def main(args: Array[String]): Unit = {
    println(1) // 1
    println(1 + 1) // 2
    println("Hello!") // Hello!
    println("Hello," + " World!") // Hello, World!

    // Value vs. variable
    val value: Int = 1 + 1
//    value = 3 // Cannot assign again
    var variable: Int = 1 + 1
    variable = 3

    // Blocks
    println({
      val x = 1 + 1
      x + 1
    }) // 3

    // Functions
    val addOne = (x: Int) => x + 1
    println(addOne(4))
    val add = (x: Int, y: Int) => x + y
    println(add(1, 2)) // 3

    // Methods
    println(add(1, 2)) // 3
    println(addThenMultiply(1, 2)(3)) // 9
    println(getSquareString(2.5))

    // Classes
    val greeter = new Greeter("Hello, ", "!")
    greeter.greet("Scala developer") // Hello, Scala developer!
  }

  private def addThenMultiply(x: Int, y: Int)(multiplier: Int): Int = (x + y) * multiplier

  private def getSquareString(input: Double): String = {
    val square = input * input
    square.toString
  }

  private def add(x: Int, y: Int): Int = x + y
}

class Greeter(prefix: String, suffix: String) {
  def greet(name: String): Unit =
    println(prefix + name + suffix)
}
