public class Factorial {
    public static void main(String[] args) {
        int number = 0;
        int factorial;

        if (args.length > 0) {
            number = Integer.parseInt(args[0]);
        }

        factorial = 1;
        for (int i = 1; i <= number; i++) {
            factorial *= i;
        }

        System.out.println(factorial);
    }
}
