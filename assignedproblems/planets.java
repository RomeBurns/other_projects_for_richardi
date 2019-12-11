import java.util.Scanner;
public class planets{
    public static void main( String[] args ) {
        Scanner keyboard = new Scanner(System.in);
        int weight, planet;
        System.out.println("What is your weight on earth in pounds?");
        weight = keyboard.nextInt();
        System.out.println("Out of the following planets, type the corresponding numbe to the planet you want your weight in. \n1:Venus    2:Mars    3:Jupiter    4:Saturn    5:Uranus    6:Neptune \nChosen Planet:");
        planet = keyboard.nextInt();
        if (planet == 1) {
            System.out.println(weight * 0.78);
        }
        else if (planet == 2) {
            System.out.println(weight * 0.39);
        }
        else if (planet == 3) {
            System.out.println(weight * 2.65);
        }
        else if (planet == 4) {
            System.out.println(weight * 1.17);
        }
        else if (planet == 5) {
            System.out.println(weight * 1.05);
        }
        else if (planet == 5) {
            System.out.println(weight * 1.23);
        }
        System.out.println("Next time use the metric system and we won't have this problem.");
    }
}