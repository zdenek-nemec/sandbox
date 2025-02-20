package cz.zdenek.sandbox.demos

import java.io.File

object ListDir {
  def main(args: Array[String]): Unit = {
    println("ListDir")
    countFiles()
  }

  def countFiles(): Unit = {
    val pwd = System.getProperty("user.dir")
    val dir = new File(pwd)
    println("Current directory: " + pwd)
    println("Items: " + dir.list().length)
    dir.list().foreach(println)
  }
}
