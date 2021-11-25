import java.util.Scanner;

public class Automat {
    public static void main(String[] args){
        //get user Data
        String userName = stringInput();
        System.out.print("What's your budget? ");
        int userMoney = intInput();
        System.out.print("How long we fly? ");
        int userDist = intInput();
        boolean returnToHome = boolInput();

        //Create user Obj & set it up
        User user1 = new User(userName, userMoney, userDist, returnToHome);
        user1.setUp();

        //check if user wants to go two ways
        user1.twoWay();

        selectTicket(user1);
        //System.out.println(user1.name + " " + user1.money + " " + user1.targetDestDist + " " + user1.targetDestDistHome);
    }

    public static String stringInput(){
        System.out.print("What's your name? ");
        Scanner scanner = new Scanner(System.in);
        String strVal = scanner.nextLine();
        return strVal;
    }

    public static int intInput(){
        Scanner scanner = new Scanner(System.in);
        int intVal = scanner.nextInt();
        return intVal;
    }

    public static boolean boolInput(){
        System.out.print("Wanna ride home? | 1: Yes | 2: No\n=> ");
        Scanner scanner = new Scanner(System.in);
        int intVal = scanner.nextInt();

        if(intVal == 1){
            return true;
        }else if(intVal == 2){
            return false;
        }else{
            System.out.println("I said 1 or 2 dummy!");
            boolInput();
        }
        return false;
    }

    public static void selectTicket(User user){
        /*
        * get dist & budget √
        * let user choose ticket and tell him if he can afford it
        * loop through tickets and find optimal ticket combo if there's one
        *
        */

        //Show ticket options
        System.out.println("Willkommen bei Thor. Unser Service ist DER Hammer\nTicket Options: \n");
        for(int i = 0; i < user.ticketArr.length; i++) {
            System.out.println(
                    "Name: " + user.ticketArr[i].name +
                    " | Cost: " + user.ticketArr[i].cost +
                    " | Distance rideable: " + user.ticketArr[i].reach +
                    " | Call Sign: " + user.ticketArr[i].callSign
            );
        }System.out.println("\n");

        //Make ticket check
        user.check();
    }
}
