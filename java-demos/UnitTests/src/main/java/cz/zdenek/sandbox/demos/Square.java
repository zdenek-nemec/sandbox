package cz.zdenek.sandbox.demos;

public class Square {
    private final int side;

    public Square(int side) {
        this.side = side;
    }

    public int getSide() {
        return this.side;
    }

    public int getArea() {
        return this.side * this.side;
    }
}
