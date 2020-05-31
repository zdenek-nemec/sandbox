public class Armstrong {
    public static void main(String[] args) {
        String number;
        int sum;

        number = "0";
        if (args.length > 0) {
            number = args[0];
        }

        sum = 0;
        for (int i = 0; i < number.length(); i++) {
            sum += Math.pow((number.charAt(i) - '0'), number.length());
        }

        if (sum == Integer.parseInt(number)) {
            System.out.println("Armstrong number");
        }
        else {
            System.out.println("not Armstrong number");
        }

    }
}
