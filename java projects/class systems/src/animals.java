abstract public class animals {
    public String name;
    public String noise;

    animals(String name){
        this.name = name;
    }

    void makeNoise(){
        System.out.println("The " + name + " " + noise + "s");
    }
}