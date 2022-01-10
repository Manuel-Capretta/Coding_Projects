import java.util.Scanner;

public class Lager {

    public static void main(String[] args){

        store obj = new store();

        lagerAblauf(obj);
    }

    public static void lagerAblauf(store obj){

        String iAsk = inputAsk();

        switch (iAsk){
            case "1" -> obj.produktEinfuegen();
            case "2" -> obj.produktEinsehen();
            case "3" -> obj.produktBearbeiten();
            case "4" -> obj.deleteProdukt();
            case "5" ->{
                System.out.println("Das Programm wird gestoppt.");
                System.exit(0);
            }
            default -> System.out.println("Falsche Eingabe, versuchen sie es nochmal");
        }
        lagerAblauf(obj);
    }

    public static String inputAsk(){
        System.out.println("Wollen sie ein neues Produkt einfügen, die andere einsehen oder das Programm stoppen.\nFür neues Produkt drücken Sie die 1\nFür Produkte einsehen drücken Sie die 2\nFür das bearbeiten eines Produktihnalts drücken Sie bitte die 3\nFür das löschen eines Produktes drücken Sie die 4\n Für das Stoppen des Programms drücken Sie die 5\nIhre Eingabe: ");
        Scanner scanner = new Scanner(System.in);
        return scanner.next();
    }
}