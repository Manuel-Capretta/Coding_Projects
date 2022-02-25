public class linObj extends depObject {
    linObj(String name, float value, int year) {
        super(name, value, year);
        type = "l";
    }

    @Override
    void calculate(float num, float percentage){
        //write off currValue for the amount of years
        for(int i = 0; i < num; i++){
            if(currValue > 0) {
                currValue -= (oldValue / 100) * percentage;
            } else {
                System.out.println("The " + name + " is written off");
                break;
            }
            log.add(currValue);
        }

        if(currValue > 0) {
            System.out.println("In the year " + (num + year -1) + ", the " + name + " has a value of " + Math.round(currValue*100.0)/100.0 + "$");
        } else {
            System.out.println("In the year " + (num + year -1) + ", the " + name + " will be written off");
        }
    }
}
