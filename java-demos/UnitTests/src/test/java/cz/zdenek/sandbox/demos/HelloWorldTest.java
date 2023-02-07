package cz.zdenek.sandbox.demos;

import junit.framework.Test;
import junit.framework.TestCase;
import junit.framework.TestSuite;

public class HelloWorldTest extends TestCase {
    public HelloWorldTest(String testName) {
        super(testName);
    }

    public static Test suite() {
        return new TestSuite(HelloWorldTest.class);
    }

    public void testHelloWorld() {
        assertTrue(true);
    }

    public void testGet4() {
        int x = HelloWorld.get4();
        assertEquals(4, x);
    }
}
