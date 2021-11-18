import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;

public class playingField extends JFrame implements KeyListener, ActionListener {
    user user1 = new user(); //user
    user user2 = new user(); //user
    int field1;
    int field2;

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

        if(!user1.inputDone){
            System.out.println("Getting user input of user 1...");
            field1 = user1.userInput(); // User 1 input
            if(field1 == field2){ //prevent a field from being used by 2 ppl
                System.out.println("This field is already used by User 2");
                field1 = user1.userInput();
            } else {
                gameMaster.tileArr[field1 - 1].xOn = true; //tell the used tile to show X
            }
            user1.inputDone = true;
            user2.inputDone = false;
            gameMaster.callSignChange();
            gameMaster.drawGrid(draw);
        } else if(!user2.inputDone){
            field2 = user2.userInput(); // User 2 input
            if(field1 == field2){ //prevent a field from being used by 2 ppl
                System.out.println("This field is already used by User 1");
                field2 = user2.userInput();
            } else {
                gameMaster.tileArr[field2 - 1].oOn = true; //tell the used tile to show O
            }
            user1.inputDone = false;
            user2.inputDone = true;
            gameMaster.callSignChange();
            gameMaster.drawGrid(draw);
        }

        //check if user 1 has won
        if(gameMaster.tileArr[0].xOn && gameMaster.tileArr[1].xOn && gameMaster.tileArr[2].xOn){
            System.out.println("User 1 Won!");
        } else {
            System.out.println("It's a draw");
            repaint();
        }
    }

    @Override
    public void actionPerformed(ActionEvent e) {

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
