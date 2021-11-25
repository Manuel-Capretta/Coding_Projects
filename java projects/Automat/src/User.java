import java.util.Scanner;

public class User {
    String name;
    double money;
    int targetDestDist;
    boolean targetDestDistHome;

    Ticket ticketArr[] = new Ticket[3];

    User(String name, double money, int targetDestDist, boolean targetDestDistHome){
        this.name = name;
        this.money = money;
        this.targetDestDist = targetDestDist;
        this.targetDestDistHome = targetDestDistHome;
    }

    void setUp(){
        //Create Tickets
        Ticket shortDist = new Ticket("S", "Short Distance", 2.5, 2);
        Ticket longDist = new Ticket("L", "Long Distance", 4, 4);
        Ticket daily = new Ticket("D", "Daily", 9, 10);

        //Put tickets in array
        ticketArr[0] = shortDist;
        ticketArr[1] = longDist;
        ticketArr[2] = daily;
    }

    void twoWay(){
        if(targetDestDistHome){
            targetDestDist*=2;
        }
    }

    void check(){
        //Let user decide what he wants aka. SBB Style
        System.out.print("Choose your Ticket: ");
        Scanner scanner = new Scanner(System.in);
        String strVal = scanner.nextLine();
        for(int i = 0; i < ticketArr.length; i++)
        if (strVal.equals(ticketArr[i].callSign) /*&& user.money >= cost*/){
            if(targetDestDist > ticketArr[i].reach){
                System.out.println("it will reach but u need more");
            } else if(targetDestDist == ticketArr[i].reach) {
                System.out.println("Excellent choice");
            }else{
                System.out.println("ticket won't reach");
            }
        }else{
            System.out.println("Gimma da valid callsingn");
        }
    }
}
