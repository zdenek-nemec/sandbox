import static org.junit.jupiter.api.Assertions.*;

class RoundToTheNextMultipleOf5Test {

    @org.junit.jupiter.api.BeforeEach
    void setUp() {
    }

    @org.junit.jupiter.api.AfterEach
    void tearDown() {
    }

    @org.junit.jupiter.api.Test
    void testRoundToNext5Zero() {
        assertEquals(0, RoundToTheNextMultipleOf5.roundToNext5(0));
    }

    @org.junit.jupiter.api.Test
    void testRoundToNext5Possitive() {
        assertEquals(5, RoundToTheNextMultipleOf5.roundToNext5(2));
        assertEquals(5, RoundToTheNextMultipleOf5.roundToNext5(3));
        assertEquals(15, RoundToTheNextMultipleOf5.roundToNext5(12));
        assertEquals(25, RoundToTheNextMultipleOf5.roundToNext5(21));
    }

    @org.junit.jupiter.api.Test
    void testRoundToNext5Negatives() {
        assertEquals(0, RoundToTheNextMultipleOf5.roundToNext5(-2));
        assertEquals(-5, RoundToTheNextMultipleOf5.roundToNext5(-5));
    }
}
