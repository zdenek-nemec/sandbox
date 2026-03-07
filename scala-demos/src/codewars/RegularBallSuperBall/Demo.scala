package cz.zdenek.sandbox.demos
package codewars.RegularBallSuperBall

object Demo {
  def main(args: Array[String]): Unit = {
    println("Regular Ball Super Ball")

    val ball = new Ball()
    println(ball.ballType)

    val ball2 = new Ball("super")
    println(ball2.ballType)
  }
}
