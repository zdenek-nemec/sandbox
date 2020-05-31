import java.util.Random;


public class SelectionSort {
    private static int[] addIntoArray(int[] array, int number) {
        int[] newArray = new int[array.length + 1];
        System.arraycopy(array, 0, newArray, 0, array.length);
        newArray[newArray.length - 1] = number;
        return newArray;
    }

    private static int getIndexOfLeast(int[] numbers) {
        int minIndex;
        minIndex = 0;
        for (int i = 0; i < numbers.length; i++) {
            if (numbers[i] < numbers[minIndex]) {
                minIndex = i;
            }
        }
        return minIndex;
    }

    private static int[] removeFromArray(int[] array, int index) {
        int[] newArray = new int[array.length - 1];
        if (newArray.length > 0) {
            System.arraycopy(array, 0, newArray, 0, index);
            System.arraycopy(array, index + 1, newArray, index, array.length - index - 1);
        }
        return newArray;
    }

    public static void main(String[] args) {
        int[] unsorted;
        int[] sorted;

        if (args.length > 0) {
            unsorted = new int[args.length];
            for (int i = 0; i < args.length; i++) {
                unsorted[i] = Integer.parseInt(args[i]);
            }
        }
        else {
            unsorted = new int[5];
            Random rand = new Random();
            for (int i = 0; i < unsorted.length; i++) {
                unsorted[i] = rand.nextInt(100);
            }
        }

        System.out.println("Before:");
        for (int value : unsorted) {
            System.out.print(value + " ");
        }
        System.out.println();

        sorted = new int[0];
        while (unsorted.length > 0) {
            int index = SelectionSort.getIndexOfLeast(unsorted);
            sorted = SelectionSort.addIntoArray(sorted, unsorted[index]);
            unsorted = SelectionSort.removeFromArray(unsorted, index);
        }

        System.out.println("After:");
        for (int value : sorted) {
            System.out.print(value + " ");
        }
        System.out.println();
    }
}
