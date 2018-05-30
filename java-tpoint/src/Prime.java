public class Prime {
    public static void main(String[] args) {
        int number = 0;
        boolean isPrime = true;

        if (args.length > 0) {
            number = Integer.parseInt(args[0]);
        }

        for (int i = 2; i < Math.sqrt(number); i++) {
            if (number % i == 0) {
                isPrime = false;
                break;
            }
        }

        if (isPrime) {
            System.out.println("prime number");
        }
        else {
            System.out.println("not prime number");
        }
    }
}
