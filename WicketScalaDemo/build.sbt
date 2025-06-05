ThisBuild / version := "0.1.0-SNAPSHOT"

ThisBuild / scalaVersion := "2.13.16"

lazy val root = (project in file("."))
  .settings(
    name := "WicketScalaDemo",
    idePackagePrefix := Some("org.zdenek")
  )

libraryDependencies ++= Seq(
  "org.apache.wicket" % "wicket-core" % "9.15.0",
//  "org.eclipse.jetty" % "jetty-server" % "11.0.20",
//  "org.eclipse.jetty" % "jetty-servlet" % "11.0.20"
)

libraryDependencies += "org.eclipse.jetty" % "jetty-server" % "9.4.54.v20240208"
libraryDependencies += "org.eclipse.jetty" % "jetty-servlet" % "9.4.54.v20240208"
libraryDependencies += "javax.servlet" % "javax.servlet-api" % "4.0.1"
