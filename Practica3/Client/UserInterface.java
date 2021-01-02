package Client;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

//Part gràfica on es posa el Swing
public class UserInterface extends JFrame{
    public UserInterface(){
        DefaultListModel<String> messages = new DefaultListModel<>();
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setSize(400, 300);//800 600

        setLayout(new GridBagLayout());

        JList<String> messageList = new JList<>(messages);
        messageList.setFixedCellWidth(325);
        add(messageList, genGrid(0, 1, 4, 1)); //Mostra l'historial del chat
        

        JTextField messageTextField = new JTextField(30);
        add(messageTextField, genGrid(0, 2, 4, 1));

        JButton sendMessageButton = new JButton("Send message");
        sendMessageButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent arg0) {
                String message = messageTextField.getText();
                messageTextField.setText("");
                //Faltaria posar nom d'ususari que envia
                messages.addElement(message);
                System.out.println(messages.getSize());
                //Control perquè no es desconfiguri la finestra
                if (messages.getSize() > 10){
                    messages.remove(0);
                }
            }
        });
        add(sendMessageButton, genGrid(0, 3, 4, 1));
        setVisible(true);
    }

    private GridBagConstraints genGrid(int x, int y, int width, int height) {
        GridBagConstraints c = new GridBagConstraints();
        c.gridx = x;
        c.gridy = y;
        c.gridwidth = width;
        c.gridheight = height;
        return c;
    }    
}
