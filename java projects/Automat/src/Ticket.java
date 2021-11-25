import java.util.Scanner;

public class Ticket {
    String callSign;
    String name;
    double cost;
    int reach;

    Ticket(String callSign, String name, double cost, int reach){
        this.callSign = callSign;
        this.name = name;
        this.cost = cost;
        this.reach = reach;
    }
}
