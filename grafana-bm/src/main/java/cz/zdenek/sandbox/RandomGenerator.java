package cz.zdenek.sandbox;

import java.util.Random;

public class RandomGenerator {
    private static final String CHARACTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";

    public static String getString(int length) {
        StringBuilder stringBuilder = new StringBuilder(length);
        Random random = new Random();
        for (int i = 0; i < length; i++) {
            int randomIndex = random.nextInt(CHARACTERS.length());
            char randomChar = CHARACTERS.charAt(randomIndex);
            stringBuilder.append(randomChar);
        }
        return stringBuilder.toString();
    }

    public static int getInt(int max) {
        return (int) Math.floor(Math.random() * max);
    }

    public static void main(String[] args) {
        System.out.println("Random string: " + getString(10));
        System.out.println("Random integer: " + getInt(1000));
    }
}
