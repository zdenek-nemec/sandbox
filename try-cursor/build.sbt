name := "try-cursor-wicket"

version := "0.1"

scalaVersion := "2.13.12"

libraryDependencies ++= Seq(
  "org.apache.wicket" % "wicket-core" % "9.15.0",
  "org.eclipse.jetty" % "jetty-server" % "9.4.54.v20240208",
  "org.eclipse.jetty" % "jetty-servlet" % "9.4.54.v20240208",
  "javax.servlet" % "javax.servlet-api" % "3.1.0" % "provided"
) 