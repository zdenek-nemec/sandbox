public class Fibonacci {
    public static final int STEPS = 10;

    public static void main(String[] args) {
        int steps = STEPS;
        int number = 0;
        int last = 0;

        if (args.length > 0) {
            steps = Integer.parseInt(args[0]);
        }

        for (int i = 0; i < steps; i++) {
            System.out.print(number + " ");
            if (i == 0) {
                last = 0;
                number = 1;
            }
            else {
                number += last;
                last = number - last;
            }
        }
    }
}
