public class RoundToTheNextMultipleOf5 {
    public static void main(String[] args) {
        System.out.println("Round up to the next multiple of 5");

        System.out.println(roundToNext5(12) + " 15");
        System.out.println(roundToNext5(15) + " 15");
        System.out.println(roundToNext5(-7) + " -5");
        System.out.println(roundToNext5(-1) + " 0");
    }

    public static int roundToNext5(int number) {
        int rem = number % 5;
        if (rem == 0) {
            return number;
        } else if (rem > 0) {
            return number + (5 - rem);
        } else {
            return number - rem;
        }
    }
}
