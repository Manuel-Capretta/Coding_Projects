import java.awt.*;

public class tile {

    //tile variables
    public int x;
    public int y;
    public int size;
    public String call;
    public boolean xOn;
    public boolean oOn;


    public tile(int x, int y, int size, String call){
        this.x = x;
        this.y = y;
        this.size = size;
    }

    public void drawTile(Graphics draw){
        draw.drawRect(x, y, size, size);
        draw.drawString(call, x+20, y+30);
    }

}
