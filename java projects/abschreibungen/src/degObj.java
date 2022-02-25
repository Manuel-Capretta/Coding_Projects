public class degObj extends depObject {
    degObj(String name, float value, int year) {
        super(name, value, year);
        type = "d";
    }

    @Override
    void calculate(float num, float percentage){

        //write off currValue for the amount of years
        for(int i = 0; i < num; i++){
            currValue = (currValue / 100) * percentage;
            log.add(currValue);
        }

        System.out.println("In the year " + (num + year -1) + ", the " + name +  " has a value of " + Math.round(currValue*100.0)/100.0 + "$");
    }
}
