import java.util.Scanner;

public class littlequiz {
    public static void main( String[] args ) {
        Scanner keyboard = new Scanner(System.in);
        int ans0, ans1, ans2, count = 0;
        System.out.println("Are you ready for a quiz? You don't actually have a choice if you want this program to run.");

        System.out.println("What is the capital of Alaska? Enter in option numbers. \n1: Melbourne\n2:Anchorage \n3:Juneau \n");
        ans0 = keyboard.nextInt();

        if (ans0 == 3) {
            count ++;
            System.out.println("Correct");
        }
        else {
            System.out.println("WRONG");
        }

        System.out.println("Can you store the value \"cat\" in a variable type int? \n1:Yes\n2:No\n");
        ans1 = keyboard.nextInt();

        if (ans1 == 2) {
            System.out.println("Correct");
            count ++;
        }
        else {
            System.out.println("False");
        }

        System.out.println("What is 9+6/3 equal to? Input only integer responses\n");
        ans2 = keyboard.nextInt();

        if (ans2 == 11) {
            System.out.println("Corrrect");
            count ++;
        }
        else {
            System.out.println("WRONG");
        }
        System.out.println("You got " + count + " answers right.");
    }
}