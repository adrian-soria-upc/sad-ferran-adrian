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
        setSize(800, 600);

        setLayout(new GridBagLayout());

        JLabel title = new JLabel("Welcome, you can start!");
        title.setFont(new Font("Titulo", Font.BOLD, 26));
        add(title, genGrid(0, 0, 1, 1));

        //JButton startButton = new JButton("Start");
        //startButton.addActionListener(new ActionListener() {
        //    @Override
        //    public void actionPerformed(ActionEvent arg0) {
        //        title.setText("Connexion established");
        //        remove(startButton);
        //    }
        //});
        //add(startButton, genGrid(0, 1, 4, 1));

        JScrollPane scrollPane = new JScrollPane();
        scrollPane.setVerticalScrollBarPolicy(22);
        Dimension preferredSize = new Dimension(600,400);
        scrollPane.setPreferredSize(preferredSize);
        JList<String> messageList = new JList<>(messages);
        scrollPane.setViewportView(messageList);
        add(scrollPane, genGrid(0, 2, 1, 1)); //Mostra l'historial del chat
       
        JTextField messageTextField = new JTextField(30);
        add(messageTextField, genGrid(0, 3, 4, 1));

        JButton sendMessageButton = new JButton("Send message");
        sendMessageButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent arg0) {
                String message = messageTextField.getText();
                messageTextField.setText("");
                //Faltaria posar nom d'ususari que envia
                messages.addElement(message);
            }
        });
        add(sendMessageButton, genGrid(0, 4, 4, 1));

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
