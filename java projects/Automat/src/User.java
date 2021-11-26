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
        Ticket shortDist = new Ticket("s", "Short Distance", 2.5, 2);
        Ticket longDist = new Ticket("l", "Long Distance", 4, 4);
        Ticket daily = new Ticket("d", "Daily", 9, 10);

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
}
