package cz.zdenek.sandbox.demos

object Main {
  def main(args: Array[String]): Unit = {
    println("Hello, World!")


    val greeter = new DefaultTraitsGreeter()
    greeter.greet("Scala developer") // Hello, Scala developer!

    val customGreeter = new CustomizableTraitsGreeter("How are you, ", "?")
    customGreeter.greet("Scala developer") // How are you, Scala developer?
  }
}
