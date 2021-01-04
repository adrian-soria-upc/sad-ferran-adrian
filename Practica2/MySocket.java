package Practica2;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.io.PrintWriter;
import java.net.Socket;

public class MySocket {
    private final Socket socket;
    private final BufferedReader output;
    private final PrintWriter input;
    public MySocket(String nick) throws IOException {
        socket = new Socket("localhost", 1234);
        output = new BufferedReader(new InputStreamReader(socket.getInputStream()));
        input = new PrintWriter(socket.getOutputStream(), true);
        input.println(nick);
    }
    private static class Input implements Runnable {//Escriure al socket
        private final MySocket socket;
        private final BufferedReader in;
        public Input(final MySocket socket) {
            this.socket = socket;
            in = new BufferedReader(new InputStreamReader(System.in));
        }
        public void run() {
            try {
                String linia;
                while ((linia = in.readLine()) != null) {
                    socket.input.println(linia);
                }
            } catch (final IOException e) {
                e.printStackTrace();
            }
    	}
    }
    private static class Output implements Runnable {//Lectura del socket
        private final MySocket socket;
        public Output(final MySocket socket) {
            this.socket = socket;
        }
        public void run() {
            while(true) {
                try {
                System.out.println(socket.output.readLine());
                } catch (final IOException e) {
                    e.printStackTrace();
                }
            }
    	}
    }
    public static void main(final String args[]) throws IOException {
        final MySocket s = new MySocket(args[0]);     
        new Thread(new Input(s)).start();
        new Thread(new Output(s)).start();
    }
}
