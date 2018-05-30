public class Palindrome {
    public static void  main(String[] args) {
        String number = "";
        boolean isPalindrome = true;

        if (args.length > 0) {
            number = args[0];
        }

        for (int i = 0; i < (number.length() / 2); i++) {
            if (number.charAt(i) != number.charAt(number.length() - 1 - i)) {
                isPalindrome = false;
                break;
            }
        }

        if (isPalindrome) {
            System.out.println("palindrome number");
        }
        else {
            System.out.println("not palindrome number");
        }
    }
}
