import java.awt.*;

public class gameMaster {
    public tile tileArr[] = new tile[9]; //save tiles in an array

    int px = 50;
    int size = 50;

    //Create the 9 tiles
    tile tile1 = new tile(px, px, size);
    tile tile2 = new tile(px*2, px, size);
    tile tile3 = new tile(px*3, px, size);
    tile tile4 = new tile(px, px*2, size);
    tile tile5 = new tile(px*2, px*2, size);
    tile tile6 = new tile(px*3, px*2, size);
    tile tile7 = new tile(px, px*3, size);
    tile tile8 = new tile(px*2, px*3, size);
    tile tile9 = new tile(px*3, px*3, size);

    void setUp(){
        System.out.println("Setting up...");

        tileArr[0] = tile1;
        tileArr[1] = tile2;
        tileArr[2] = tile3;
        tileArr[3] = tile4;
        tileArr[4] = tile5;
        tileArr[5] = tile6;
        tileArr[6] = tile7;
        tileArr[7] = tile8;
        tileArr[8] = tile9;
    }

    /*void arrayDec(tile tile1, tile tile2, tile tile3, tile tile4, tile tile5, tile tile6, tile tile7, tile tile8, tile tile9){
        //Add the tiles to the tiles array
        tileArr[0] = tile1;
        tileArr[1] = tile2;
        tileArr[2] = tile3;
        tileArr[3] = tile4;
        tileArr[4] = tile5;
        tileArr[5] = tile6;
        tileArr[6] = tile7;
        tileArr[7] = tile8;
        tileArr[8] = tile9;
    }*/

    void callSignChange(){
        for(int i = 0; i < 9; i++) {
            //Check if tile has a letter on it
            if (tileArr[i].xOn) {
                tileArr[i].call = "X";
            } else if (tileArr[i].oOn) {
                tileArr[i].call = "O";
            } else {
                tileArr[i].call = " ";
            }
        }
    }

    void drawGrid(Graphics draw){
        for(int i = 0; i < 9; i++){
            tileArr[i].drawTile(draw);
        }
    }
}
