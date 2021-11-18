import java.util.Scanner;

public class user {

    boolean inputDone = false; //this allows for a repaint to only be possible if a user gave an input
    Scanner scan = new Scanner(System.in);

    int userInput(){
        int field;

        System.out.print("Input a number between 1-9: ");
        field = scan.nextInt();

        if(field > 9 || field < 1){
            System.out.println("This isn't a number between 1 and 9 dummy. Try again");
            inputDone = false;      //thus, user input won't be seen as done
            field = userInput();
        }

        inputDone = true;
        return field;
    }
}
