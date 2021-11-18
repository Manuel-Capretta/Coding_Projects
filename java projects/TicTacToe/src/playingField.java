import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;

public class playingField extends JFrame implements KeyListener, ActionListener {
    user user1 = new user(); //user

    public playingField() {
        setTitle("Snake Game Board");
        setSize(500, 500);
        setResizable(false);
        setVisible(true);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        addKeyListener(this);
        /*Timer t = new Timer(1000000000, this);
        t.start();*/
    }

    public void paint(Graphics draw) {
        gameMaster gameMaster = new gameMaster();
        gameMaster.setUp(); //setup all the tiles etc
        //user1.userInput();
        gameMaster.tileArr[5-1].xOn = true; //Put an X in the middle of the field
        gameMaster.callSignChange();
        gameMaster.drawGrid(draw);
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        if(user1.inputDone){
            repaint(); //refresh if user input was given
        }
    }

    @Override
    public void keyTyped(KeyEvent e) {

    }

    @Override
    public void keyPressed(KeyEvent e) {

    }

    @Override
    public void keyReleased(KeyEvent e) {

    }
}
