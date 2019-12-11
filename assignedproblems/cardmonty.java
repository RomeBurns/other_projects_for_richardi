import java.util.Scanner;
import java.util.Random;

public class cardmonty {
    public static void main( String[] args ) {
        Scanner keyboard = new Scanner(System.in);
        int val, rand, g, i = 0;
        System.out.println("How many cards do you want to guess from? ");
        val = keyboard.nextInt();
        Random rand1 = new Random();
        rand = rand1.nextInt(val);
        while (i < val) {
            System.out.print("##  ");
            i++;
        }
        i = 0;
        System.out.println("");
        while (i < val) {
            System.out.print("##  ");
            i++;
        }
        System.out.println("");
        i = 0;
        while (i < val) {
            i++;
            System.out.print(i + "   ");

        }
        System.out.println("Which card do you think is the ace? All the others are jacks. ");
        g = keyboard.nextInt() - 1;
        if (g == rand) {
            System.out.println("Correct!");
        }
        else {
            System.out.println("False!");
        }
        i = 0;
        while (i < val) {
            if (i != rand) {
                System.out.print("JJ  ");
            }
            else {
                System.out.print("AA  ");
            }
            i++;
        }
        i = 0;
        System.out.println("");
        while (i < val) {
            if (i != rand) {
                System.out.print("JJ  ");
            }
            else {
                System.out.print("AA  ");
            }
            i++;
        }
        System.out.println("");
        i = 0;
        while (i < val) {
            i++;
            System.out.print(i + "   ");

        }
    }
}