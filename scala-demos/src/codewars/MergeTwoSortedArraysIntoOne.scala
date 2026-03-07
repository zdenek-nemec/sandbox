package cz.zdenek.sandbox.demos
package codewars

// https://www.codewars.com/kata/5899642f6e1b25935d000161/train/scala
object MergeTwoSortedArraysIntoOne {
  def mergeArrays(xs: Seq[Int], ys: Seq[Int]): Seq[Int] = (xs ++ ys).distinct.sorted

  def main(args: Array[String]): Unit = {
    println("Merge two sorted arrays into one")
    println(mergeArrays(Seq(1, 2, 3), Seq(5, 4, 3, -20)))
  }
}
