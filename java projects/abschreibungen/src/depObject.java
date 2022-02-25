import java.util.ArrayList;

abstract public class depObject {
    //Variables
    String name, type;
    int year;
    float currValue, oldValue;
    boolean belowFive;

    ArrayList<Float> log;

    depObject(String name, float value, int year){
        this.year = year;
        this.name = name;
        this.currValue = value;
        this.oldValue = value;
        this.belowFive = !(value > 500); //if value below 500, belowFive true
        log = new ArrayList<>();
    }

    void showLogs(){
        int count = 1;
        for(float f : log){
            System.out.println((year+count-1) + ": " + f);
            count++;
        }
    }

    //empty method that later will be overwritten by daughter classes
    void calculate(float num, float percentage){
        //Empty
    }
}
