package client;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Vector;
import java.io.InputStreamReader;
import javax.swing.*;

import client.UserInterface;

public class Client extends Thread {

    private String username;
    private ClientSocket socket;
    private DefaultListModel<String> messages;
    
    public Client(String username) {
        this.username = username;
        messages = new DefaultListModel<>();
    }

    public void run() {
        new UserInterface(this, messages);
    }

    public void startChat() {
        new Thread(new Runnable(){
            @Override
            public void run() {
                socket = new ClientSocket(username, messages);                
            }
        }).start();
    }
    
    public void sendMessage(String message) {
        messages.addElement(message);
        socket.sendMessage(message);
    }
    public static void main(String[] args) throws IOException {
        Client client = new Client(args[0]);
        client.start();
    }
}
