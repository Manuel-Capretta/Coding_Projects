import javax.xml.crypto.Data;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        int choice = menu();

        switch (choice) {
            case 1:
                System.out.println("lol"+choice);
                break;
            case 2:
                System.out.println("lol"+choice);
                break;
            case 3:
                System.out.println("lol"+choice);
                break;
            case 4:
                System.out.println("lol"+choice);
                break;
            default:
                System.out.println("lol"+choice);
        }
    }

    public static int menu() {
        int selection;
        Scanner input = new Scanner(System.in);



        selection = input.nextInt();
        return selection;
    }
}
