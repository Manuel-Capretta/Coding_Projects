public class LagerBestand {
    int ID;
    String name;
    int preis;
    boolean ausverkauft;

    LagerBestand(int ID, String name, int preis, boolean ausverkauft){
        this.ID = ID;
        this.name = name;
        this.preis = preis;
        this.ausverkauft = ausverkauft;
    }
}
