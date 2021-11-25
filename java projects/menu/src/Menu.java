import java.util.Scanner;

public class Menu {
    public Menu() { // Auswahl möglichkeiten erklären
        System.out.println("Wählen sie Ihre Auswahl zwischen a , b oder c");

    }
    public static String Input() { // Funktionen Auswahl input wird erstellt
        Scanner sc1 = new Scanner(System.in);
        String input = sc1.nextLine();
        return input;
    }
}