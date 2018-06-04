import java.util.Random;


public class BubbleSort {
    public static void main(String[] args) {
        int arrayLength = 5;

        if (args.length > 0) {
            arrayLength = args.length;
        }

        int[] numbers = new int[arrayLength];
        if (args.length > 0) {
            for (int i = 0; i < arrayLength; i++) {
                numbers[i] = Integer.parseInt(args[i]);
            }
        }
        else {
            Random rand = new Random();
            for (int i = 0; i < arrayLength; i++) {
                numbers[i] = rand.nextInt(100);
            }
        }

        System.out.println("Before:");
        for (int value : numbers) {
            System.out.print(value + " ");
        }
        System.out.println();

        int[] sortedNumbers = new int[arrayLength];
        System.arraycopy(numbers, 0, sortedNumbers, 0, numbers.length);

        while (true) {
            boolean hasChanged = false;
            for (int i = 0; i < sortedNumbers.length - 1; i++) {
                if (sortedNumbers[i] > sortedNumbers[i + 1]) {
                    int temp = sortedNumbers[i];
                    sortedNumbers[i] = sortedNumbers[i + 1];
                    sortedNumbers[i + 1] = temp;
                    hasChanged = true;
                }
            }
            if (!hasChanged) {
                break;
            }
        }

        System.out.println("After:");
        for (int value : sortedNumbers) {
            System.out.print(value + " ");
        }
        System.out.println();
    }
}
