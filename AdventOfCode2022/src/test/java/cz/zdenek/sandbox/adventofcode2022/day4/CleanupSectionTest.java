package cz.zdenek.sandbox.adventofcode2022.day4;

import org.junit.Assert;
import org.junit.Test;

import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;

public class CleanupSectionTest {
    @Test
    public void testSingleAssignment() {
        CleanupSection cleanupSection = new CleanupSection("2-2");
        Assert.assertEquals(Integer.valueOf(2), cleanupSection.getAssignmentsStart());
        Assert.assertEquals(Integer.valueOf(2), cleanupSection.getAssignmentsEnd());
    }

    @Test
    public void testMultipleAssignments() {
        CleanupSection cleanupSection = new CleanupSection("2-4");
        Assert.assertEquals(Integer.valueOf(2), cleanupSection.getAssignmentsStart());
        Assert.assertEquals(Integer.valueOf(4), cleanupSection.getAssignmentsEnd());
    }

    @Test
    public void testIsOverlappingFullyWithNoOverlap() {
        CleanupSection cleanupSection = new CleanupSection("2-4");
        assertFalse(cleanupSection.isOverlappingFully("0-0"));
        assertFalse(cleanupSection.isOverlappingFully("0-1"));
        assertFalse(cleanupSection.isOverlappingFully("5-6"));
        assertFalse(cleanupSection.isOverlappingFully("6-6"));
    }

    @Test
    public void testIsOverlappingFullyWithPartialLeftOverlap() {
        CleanupSection cleanupSection = new CleanupSection("2-4");
        assertFalse(cleanupSection.isOverlappingFully("1-2"));
    }

    @Test
    public void testIsOverlappingFullyWithPartialRightOverlap() {
        CleanupSection cleanupSection = new CleanupSection("2-4");
        assertFalse(cleanupSection.isOverlappingFully("4-5"));
    }

    @Test
    public void testIsOverlappingFullyWithFullOverlap() {
        CleanupSection cleanupSection = new CleanupSection("2-4");
        assertTrue(cleanupSection.isOverlappingFully("2-2"));
        assertTrue(cleanupSection.isOverlappingFully("2-3"));
        assertTrue(cleanupSection.isOverlappingFully("2-4"));
        assertTrue(cleanupSection.isOverlappingFully("3-3"));
        assertTrue(cleanupSection.isOverlappingFully("3-4"));
        assertTrue(cleanupSection.isOverlappingFully("4-4"));
    }

    @Test
    public void testIsOverlappingWithNoOverlap() {
        CleanupSection cleanupSection = new CleanupSection("2-4");
        Assert.assertFalse(cleanupSection.isOverlapping("0-0"));
        Assert.assertFalse(cleanupSection.isOverlapping("0-1"));
        Assert.assertFalse(cleanupSection.isOverlapping("5-6"));
        Assert.assertFalse(cleanupSection.isOverlapping("6-6"));
    }

    @Test
    public void testIsOverlappingWithPartialLeftOverlap() {
        CleanupSection cleanupSection = new CleanupSection("2-4");
        Assert.assertTrue(cleanupSection.isOverlapping("1-2"));
    }

    @Test
    public void testIsOverlappingWithPartialRightOverlap() {
        CleanupSection cleanupSection = new CleanupSection("2-4");
        Assert.assertTrue(cleanupSection.isOverlapping("4-5"));
    }

    @Test
    public void testIsOverlappingWithFullOverlap() {
        CleanupSection cleanupSection = new CleanupSection("2-4");
        Assert.assertTrue(cleanupSection.isOverlapping("2-2"));
        Assert.assertTrue(cleanupSection.isOverlapping("2-3"));
        Assert.assertTrue(cleanupSection.isOverlapping("2-4"));
        Assert.assertTrue(cleanupSection.isOverlapping("3-3"));
        Assert.assertTrue(cleanupSection.isOverlapping("3-4"));
        Assert.assertTrue(cleanupSection.isOverlapping("4-4"));
    }
}
