import java.util.Random;


public class LinearSearch {
    private static final int DEFAULT_ARRAY_LENGTH = 30;
    private static final int DEFAULT_RANDOM_LIMIT = 100;

    public static void main(String[] arguments) {
        boolean isSearchSuccessful = false;
        int[] array = new int[DEFAULT_ARRAY_LENGTH];
        int target;
        for (int index = 0; index < array.length; index++) {
            Random random = new Random();
            array[index] = random.nextInt(DEFAULT_RANDOM_LIMIT);
        }
        for (int value : array) {
            System.out.print(value + " ");
        }
        System.out.println();
        Random random = new Random();
        target = random.nextInt(DEFAULT_RANDOM_LIMIT);
        for (int index = 0; index < array.length; index++) {
            if (array[index] == target) {
                System.out.println("Search successful. The value " + target + " is on index " + index + ".");
                isSearchSuccessful = true;
                break;
            }
        }
        if (!isSearchSuccessful) {
            System.out.println("Search failed. The value " + target + " not found.");
        }
    }
}
