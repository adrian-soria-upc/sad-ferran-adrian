package SelectorNIO;

import java.io.IOException;
import java.net.InetSocketAddress;
import java.nio.ByteBuffer;
import java.nio.channels.*;

public class Client {
    private static SocketChannel client;
    private static ByteBuffer buffer;

    public static Client start() { 
        return new Client();
    }
 
    public static void stop() throws IOException {
        client.close();
        buffer = null;
    }
 
    private Client() {
        try {
            client = SocketChannel.open(new InetSocketAddress("localhost", 1234));
            buffer = ByteBuffer.allocate(256);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
 
    public String sendMessage(String message) {
        buffer = ByteBuffer.wrap(message.getBytes());
        String response = null;
        try {
            client.write(buffer);
            buffer.clear();
            client.read(buffer);
            response = new String(buffer.array()).trim();
            System.out.println("response = " + response);
            buffer.clear();
        } catch (IOException e) {
            e.printStackTrace();
        }
        return response;
 
    }
}
