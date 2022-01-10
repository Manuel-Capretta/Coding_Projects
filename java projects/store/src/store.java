import java.util.ArrayList;
import java.util.Scanner;

public class store {

    int ID = 0;
    ArrayList<LagerBestand> lagerProdukte  = new ArrayList<>();



    public void produktEinfuegen(){
        String iPName = inputPName();
        int iPPreis = inputPPreis();
        ID++;
        LagerBestand obj1 = new LagerBestand(ID, iPName, iPPreis, false);
        lagerProdukte.add(obj1);

        for (LagerBestand i : lagerProdukte){
            showProducts(i);
        }
    }

    public static String inputPName(){
        System.out.print("Geben Sie bitte den Produkt Namen ein: ");
        Scanner scanner = new Scanner(System.in);
        return scanner.next();
    }

    public static int inputPPreis(){
        System.out.print("Geben Sie jetzt bitte den Preis des Produktes an:");
        Scanner scanner = new Scanner(System.in);
        return scanner.nextInt();
    }

    public void produktEinsehen(){
        for (LagerBestand i : lagerProdukte){
            showProducts(i);
        }
    }

    public static int inputIdAuswaehlen(){
        System.out.println("Geben sie bitte die ID des Produktes an, dass sie bearbeiten wollen: ");
        Scanner scanner = new Scanner(System.in);
        return scanner.nextInt();
    }

    public static String inputBearbeitenName(){
        Scanner scanner = new Scanner(System.in);
        return scanner.next();
    }

    public static String inputBearbeitenPreis(){
        Scanner scanner = new Scanner(System.in);
        return scanner.next();
    }

    public void produktBearbeiten(){
        int iBearbeiten = inputIdAuswaehlen();
        int iID = iBearbeiten - 1;

        LagerBestand showProdukt = lagerProdukte.get(iID);

        showProducts(showProdukt);

        System.out.println("Ausvekauft?");
        String sold = inputBearbeitenName();

        String objName; //variable die ins objekt kommt 😛
        int objPreis; //variable die ins objekt kommt 😛
        boolean soldout;

        if(sold.equals("nein")) {
            System.out.println("Bitte geben sie jetzt die neuen werte ein.\nProduktname: ");
            String newPName = inputBearbeitenName();
            System.out.println("Produktpreis: ");
            String newPPreis = inputBearbeitenPreis();

            if (newPName.equals("")) {
                objName = showProdukt.name;
            } else {
                objName = newPName;
            }

            if (newPPreis.equals("")) {
                objPreis = showProdukt.preis;
            } else {
                objPreis = Integer.parseInt(newPPreis);
            }

            soldout = false;
        } else {
            objName = showProdukt.name;
            objPreis = showProdukt.preis;
            soldout = true;
        }

        LagerBestand temporaer = new LagerBestand(iBearbeiten, objName, objPreis, soldout);

        lagerProdukte.set(iID, temporaer);
    }

    public static int inputdelete(){
        System.out.println("Geben Sie bitte die ID des Produktes ein welches Sie löschen wollen: ");
        Scanner scanner = new Scanner(System.in);
        return scanner.nextInt();
    }

    public void deleteProdukt(){

        int inputloeschen = inputdelete();
        int iID = inputloeschen - 1;

        lagerProdukte.remove(iID);

        for(int i = iID; i < lagerProdukte.size(); i++){
            //lagerProdukte.set(i, lagerProdukte.get(i));   // -> eigentliches aufrücken ohne id
            LagerBestand temp = lagerProdukte.get(i);
            temp.ID--;
            lagerProdukte.set(i, temp);

        }
    }

    public void showProducts(LagerBestand showProdukt){
        if(!showProdukt.ausverkauft){
            System.out.print(showProdukt.ID + " " + showProdukt.name + ", " + showProdukt.preis + "CHF\n");
        }else{
            System.out.println(showProdukt.ID + " Ist gerade Ausverkauft");
        }
    }
}