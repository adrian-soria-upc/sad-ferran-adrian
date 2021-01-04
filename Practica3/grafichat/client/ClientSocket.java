package client;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;

import javax.swing.DefaultListModel;

public class ClientSocket {
    private Socket socket;
    private BufferedReader in;
    private PrintWriter out;

    public ClientSocket(String nick, DefaultListModel<String> messages){
        try {
            socket = new Socket("localhost", 1234);
            this.in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            this.out = new PrintWriter(socket.getOutputStream(), true);
            sendMessage(nick);

            new Thread(new Runnable(){
                @Override
                public void run() {
                    try {
                        String message;
                        while ((message = in.readLine()) != null) {
                            messages.addElement(message);
                        }
                    } catch (IOException e) {
                        e.printStackTrace();
                    }
                }
            }).start();

        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public void sendMessage(final String message) {
        out.println(message);
    }

    public String receiveMessage() throws IOException {
        return in.readLine();
    }
}
