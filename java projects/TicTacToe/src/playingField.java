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
    }

    public void paint(Graphics draw) {
        gameMaster gameMaster = new gameMaster();
        gameMaster.setUp(); //setup all the tiles etc
        if(!user1.inputDone) { //if no user input was done
            int field = user1.userInput(gameMaster); //user can input a field on which he wants his sign to be drawn on
            gameMaster.tileArr[field-1].xOn = true; //Put an X in the field users choice
        }
        if(user1.inputDone) { //if user has made his choice
            gameMaster.callSignChange(); //change fields call sign
        }
        System.out.println("(re)Drawing Grid now...");
        gameMaster.drawGrid(draw);
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        if(user1.inputDone){
            user1.inputDone = false;
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
