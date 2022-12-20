package cz.zdenek.sandbox.adventofcode2022.day5;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

class CrateTest {
    @Test
    void getName() {
        Crate crate = new Crate('A');
        assertEquals('A', crate.getName());
    }
}
