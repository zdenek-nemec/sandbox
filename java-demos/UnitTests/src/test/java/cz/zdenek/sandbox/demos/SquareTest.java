package cz.zdenek.sandbox.demos;

import junit.framework.Test;
import junit.framework.TestCase;
import junit.framework.TestSuite;

public class SquareTest extends TestCase {
    public SquareTest(String testName) {
        super(testName);
    }

    public static Test suite() {
        return new TestSuite(SquareTest.class);
    }

    public void testSquareGetSide() {
        Square square = new Square(2);
        int side = square.getSide();
        assertEquals(2, side);
    }

    public void testSquareGetArea() {
        Square square = new Square(2);
        int area = square.getArea();
        assertEquals(4, area);
    }
}
