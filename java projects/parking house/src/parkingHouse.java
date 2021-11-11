import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class parkingHouse extends JFrame implements ActionListener{

    public parkingHouse() {
        setTitle("Snake Game Board");
        setSize(500, 500);
        setResizable(false);
        setVisible(true);
        setDefaultCloseOperation(EXIT_ON_CLOSE);

        Timer t = new Timer(200, this);
        t.start();
    }

    public void paint(Graphics draw) {
        draw.drawRect(250, 250, 50, 50);
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        repaint(); //refresh
    }
}
