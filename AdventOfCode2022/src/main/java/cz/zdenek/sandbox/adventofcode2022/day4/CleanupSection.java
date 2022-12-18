package cz.zdenek.sandbox.adventofcode2022.day4;

public class CleanupSection {
    private static Integer assignmentsStart;
    private static Integer assignmentsEnd;

    public CleanupSection(String section) {
        assignmentsStart = parseAssignmentsStart(section);
        assignmentsEnd = parseAssignmentsEnd(section);
    }

    private Integer parseAssignmentsStart(String section) {
        String[] limits = section.split("-");
        return Integer.valueOf(limits[0]);
    }

    private Integer parseAssignmentsEnd(String section) {
        String[] limits = section.split("-");
        return Integer.valueOf(limits[limits.length - 1]);
    }

    public Integer getAssignmentsStart() {
        return assignmentsStart;
    }

    public Integer getAssignmentsEnd() {
        return assignmentsEnd;
    }

    public boolean isOverlappingFully(String section) {
        Integer requestAssignmentStart = parseAssignmentsStart(section);
        Integer requestAssignmentEnd = parseAssignmentsEnd(section);
        return (assignmentsStart <= requestAssignmentStart && assignmentsEnd >= requestAssignmentEnd) || (assignmentsStart >= requestAssignmentStart && assignmentsEnd <= requestAssignmentEnd);
    }
}
