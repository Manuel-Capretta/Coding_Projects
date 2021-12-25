public class Main{

    public static void main(String[] args){
        dog bello = new dog("Dog");
        cat xDieAgrezifeKadse = new cat("Ket");

        enimelz(bello, xDieAgrezifeKadse);
    }

    public static void enimelz(dog bello, cat xDieAgrezifeKadse){
        bello.makeNoise();
        xDieAgrezifeKadse.makeNoise();
    }
}
