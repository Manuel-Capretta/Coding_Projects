import java.util.ArrayList;
import java.util.Scanner;

public class depClass {

    public static float percentageLin;
    public static float percentageDeg;

    //list of objects
    public static ArrayList<depObject> objects = new ArrayList<>();

    public static void main(String[] args){
        //set percentages for this session
        setPercentages();

        //call user interface for the first time
        userInterface();
    }

    public static void userInterface(){

        System.out.println("(1) Create Object | (2) show Objects");
        int userInp = intInp();
        switch (userInp){
            case 1 -> createNewObject();
            case 2 -> showCalculatedResults();
            default -> {
                System.out.println("Invalid input");
                userInterface();
            }
        }
    }



    public static void createNewObject(){
        System.out.print("Name: ");
        String name = strInp();
        System.out.print("Value: ");
        int val = intInp();
        System.out.print("Year: ");
        int year = intInp();

        System.out.println("(1) degressive | (2) linear");
        int userInp = intInp();

        //add object to list depending on type of depreciation
        switch (userInp){
          case 1 -> objects.add(new degObj(name, val, year));
          case 2 -> objects.add(new linObj(name, val, year));
          default -> {
              System.out.println("Invalid input");
              createNewObject();
          }
        }

        userInterface();
    }

    public static void showCalculatedResults(){
        System.out.println("What object would you like to have calculated?\nAvailable objects: ");
        for(depObject d : objects){
            System.out.println(d.name);
        }

        String userChoice = strInp();

        for(depObject d : objects){
                if(userChoice.equals(d.name)){
                    System.out.println("\nHow many years for the " + d.name);
                    int num = intInp();

                    //check for type before calculation
                    if(d.type.equals("l")) {
                        d.calculate(num, percentageLin);
                    } else {
                        d.calculate(num, percentageDeg);
                    }
                    d.showLogs();
                    break;
                }
        }

        userInterface();
    }

    public static int intInp(){
        Scanner scan = new Scanner(System.in);
        return scan.nextInt();
    }

    public static float floInp(){
        Scanner scan = new Scanner(System.in);
        return scan.nextFloat();
    }

    public static String strInp(){
        Scanner scan = new Scanner(System.in);
        return scan.nextLine();
    }

    public static void setPercentages(){
        System.out.println("Please input the percentages for the two types of depreciation");
        System.out.print("Degressive: ");
        percentageDeg = floInp();
        System.out.print("Linear: ");
        percentageLin = floInp();
    }
}
