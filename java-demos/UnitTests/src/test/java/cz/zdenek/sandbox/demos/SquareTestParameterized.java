package cz.zdenek.sandbox.demos;

import org.junit.Before;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.junit.runners.Parameterized;

import java.util.Arrays;
import java.util.Collection;

import static org.junit.Assert.assertEquals;

@RunWith(Parameterized.class)
public class SquareTestParameterized {
    private final int side;
    private final int expectedArea;
    private Square square;

    public SquareTestParameterized(int side, int expectedArea) {
        this.side = side;
        this.expectedArea = expectedArea;
    }

    @Parameterized.Parameters
    public static Collection areas() {
        return Arrays.asList(new Object[][]{
                {0, 0},
                {1, 1},
                {2, 4},
                {3, 9}
        });
    }

    @Before
    public void initialize() {
        square = new Square(0);
    }

    @Test
    public void testSquareGetArea() {
        int area = square.getArea(this.side);
        assertEquals(this.expectedArea, area);
    }
}
