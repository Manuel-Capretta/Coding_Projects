import java.util.Scanner;

public class user {

    boolean inputDone = false; //this allows for a repaint to only be possible if a user gave an input
    Scanner scan = new Scanner(System.in);

    int userInput(gameMaster gameMaster){
        System.out.println("User input will be ready soon...");

        int field;

        System.out.print("Input a number between 1-9: ");
        field = scan.nextInt();

        if(field > 9 || field < 1){
            System.out.println("This isn't a number between 1 and 9 you dummy ;)\n");
            userInput(gameMaster);
        } else {
            inputDone = true;
            return field;
        }
        return field;
    }
}
