import java.util.Scanner;

public class user {

    boolean inputDone = false; //this allows for a repaint to only be possible if a user gave an input
    Scanner scan = new Scanner(System.in);

    int userInput(){
        int field;

        System.out.print("Input a number between 1-9: ");
        field = scan.nextInt();

        while(field > 9 || field < 1){
            field = scan.nextInt(); //rescan if number isn't valid
            inputDone = false;      //thus, user input won't be seen as done
        }

        inputDone = true;
        return field;
    }
}
