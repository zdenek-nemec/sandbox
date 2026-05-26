package cz.zdenek.sandbox.demos
package codewars

// https://www.codewars.com/kata/55ecd718f46fba02e5000029/train/scala
object WhatIsBetween {
  def between(a: Int, b: Int): Seq[Int] = {
    val result = for (i <- a to b) yield i
    result.toSeq
  }

  def main(args: Array[String]): Unit = {
    println("What is between?")
    val result = between(1, 5)
    println(result)
    println(s"${result.getClass}")
  }
}
