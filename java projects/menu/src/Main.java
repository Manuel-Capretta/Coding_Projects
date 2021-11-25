public class Main {

    public static void main(String[] args) {
        Run();

    }
    public static void Run() {
        new Menu();
        String input = Menu.Input();
        // Checkt ob der input verfügbar ist
        if(input.equals("a") || input.equals("b") || input.equals("c")){ //Wenn  ja dann ruft es die Funktion Selection auf
            Selection(input);
        } else { // Sonnst ruft es die Funktion invalid auf
            invalid();

        }
    }
    public static void Selection(String input) {
        while(input != null) { // Infinite loop
            switch (input) { // Wenn input a , b oder c ist wird die dazu gehörige Funktion aufgerufen
                case "a":
                    new Item().Item1();
                    Run();
                    break;
                case "b":
                    new Item().Item2();
                    Run();
                    break;
                case "c":
                    new Item().Item3();
                    Run();
                    break;
            }
        }
    }
    public static void invalid() {
        System.out.println("Your Choice was Invalid");
    }
}

