import java.util.Scanner;

public class user {
    Scanner scan = new Scanner(System.in);
    int field;
    boolean inputDone = false; //this allows for a repaint to only be possible if a user gave an input

    void userInput(){
        field = scan.nextInt();

        System.out.print("Input a number between 1-9: ");
        if(field > 9 || field < 1){
            System.out.println("This isn't a number between 1 and 9 you dummy ;)\n");
            userInput();
        } else {
            inputDone = true;
        }
    }
}
