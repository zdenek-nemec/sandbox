import java.util.Random;


public class InsertionSort {
    private static final int DEFAULT_ARRAY_LENGTH = 5;
    private static final int DEFAULT_RANDOM_LIMIT = 100;

    private static boolean isCalledWithArguments(int length) {
        return (length > 0);
    }

    private static int[] loadInput(String[] arguments) {
        if (isCalledWithArguments(arguments.length)) {
            return parseInput(arguments);
        } else {
            return generateNumbers();
        }
    }

    private static int[] generateNumbers() {
        int[] array = new int[DEFAULT_ARRAY_LENGTH];
        for (int i = 0; i < array.length; i++) {
            array[i] = getRandomNumber();
        }
        return array;
    }

    private static int getProperPosition(int[] array, int value) {
        for (int i = 0; i < array.length; i++) {
            if (array[i] >= value) {
                return i;
            }
        }
        return array.length;
    }

    private static int getRandomNumber() {
        Random random = new Random();
        return random.nextInt(DEFAULT_RANDOM_LIMIT);
    }

    private static int[] insertValue(int[] array, int value, int position) {
        int[] newArray = new int[array.length + 1];
        System.arraycopy(array, 0, newArray, 0, position);
        newArray[position] = value;
        System.arraycopy(array, position, newArray, position + 1, array.length - position);
        return newArray;
    }

    private static int[] parseInput(String[] arguments) {
        int[] array = new int[arguments.length];
        for (int i = 0; i < arguments.length; i++) {
            array[i] = Integer.parseInt(arguments[i]);
        }
        return array;
    }

    private static void printArray(int[] array) {
        for (int value : array) {
            System.out.print(value + " ");
        }
        System.out.println();
    }

    private static int[] sort(int[] unsorted) {
        int[] sorted = new int[0];
        for (int value : unsorted) {
            int position = getProperPosition(sorted, value);
            sorted = insertValue(sorted, value, position);
        }
        return sorted;
    }

    public static void main(String[] arguments) {
        int[] unsorted;
        int[] sorted;
        unsorted = loadInput(arguments);
        System.out.println("Before:");
        printArray(unsorted);
        sorted = sort(unsorted);
        System.out.println("After:");
        printArray(sorted);
    }
}
