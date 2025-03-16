package cz.zdenek.sandbox.demos

trait TraitsGreeter {
  def greet(name: String): Unit =
    println("Hello, " + name + "!")
}

class DefaultTraitsGreeter extends TraitsGreeter

class CustomizableTraitsGreeter(prefix: String, postfix: String) extends TraitsGreeter {
  override def greet(name: String): Unit = {
    println(prefix + name + postfix)
  }
}

object BasicsTraits {
  def main(args: Array[String]): Unit = {
    println("BasicsTraits")

    val greeter = new DefaultTraitsGreeter()
    greeter.greet("Scala developer") // Hello, Scala developer!

    val customGreeter = new CustomizableTraitsGreeter("How are you, ", "?")
    customGreeter.greet("Scala developer") // How are you, Scala developer?
  }
}
