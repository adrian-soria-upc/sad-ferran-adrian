package server;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.Map;
import java.util.HashMap;

public class Server {
    private Map<String, Socket> users;
    private ServerSocket ss;

    public Server() throws IOException {
        ss = new ServerSocket(1234);
        users = new HashMap<>();
    }

    public void listen() throws IOException {
        while (true) {
            Socket s = ss.accept();
            new Thread(new Helper(s)).start();
        }
    }
    private class Helper implements Runnable {
        private Socket s;
        private BufferedReader output;
        private PrintWriter input;
        public Helper(Socket s) throws IOException {
            this.s=s;
            output = new BufferedReader(new InputStreamReader(s.getInputStream()));
            input = new PrintWriter(s.getOutputStream(), true);
        }
        public void run() {
            try {
                String nick = output.readLine();
                users.put(nick, s);
                System.out.println(nick + " connected");
                input.println("Welcome");
                String linia;
                while ((linia = output.readLine()) != null) {
                    System.out.println(nick + "> " + linia);
                    for (Socket value : users.values()) {
                        if (value != s) {
                            PrintWriter in = new PrintWriter(value.getOutputStream(), true);
                            in.println(nick + "> " + linia);
                        }
                    }
                }
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }
    public static void main(String[] args) throws IOException {
        Server serverSocket = new Server();
        serverSocket.listen();
    }
} 
