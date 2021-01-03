package SelectorNIO;

import java.io.*;
import java.net.*;
import java.nio.*;
import java.nio.channels.*;
import java.util.*;

public class Server {
    Selector selector ;
    ServerSocketChannel serverSocket ;
    ByteBuffer buffer;
    
    public Server () throws IOException {
        selector = Selector.open();
        serverSocket = ServerSocketChannel.open();
        serverSocket.bind(new InetSocketAddress("localhost", 1234));
        serverSocket.configureBlocking(false);
        serverSocket.register(selector, SelectionKey.OP_ACCEPT);
        buffer = ByteBuffer.allocate(256);
    }

    public void listen(ByteBuffer buffer) throws IOException {
        while (true) {
            selector.select();
            Set<SelectionKey> selectedKeys = selector.selectedKeys();
            Iterator<SelectionKey> iter = selectedKeys.iterator();
            while (iter.hasNext()) {
 
                SelectionKey key = iter.next();
 
                if (key.isAcceptable()) {
                    register(selector, serverSocket);
                }
 
                if (key.isReadable()) {
                    answerWithEcho(buffer, key);
                }
                iter.remove();
            }
        }
    }

    private static void answerWithEcho(ByteBuffer buffer, SelectionKey key) throws IOException {
        SocketChannel client = (SocketChannel) key.channel();
        client.read(buffer);
        if (new String(buffer.array()).trim().equals("POISON_PILL")) {
            client.close();
            System.out.println("Not accepting client messages anymore");
        }

        buffer.flip();
        client.write(buffer);
        buffer.clear();
    }
 
    private static void register(Selector selector, ServerSocketChannel serverSocket)
      throws IOException {
  
        SocketChannel client = serverSocket.accept();
        client.configureBlocking(false);
        client.register(selector, SelectionKey.OP_READ);
    }
 
    public static Process start() throws IOException, InterruptedException {
        String javaHome = System.getProperty("java.home");
        String javaBin = javaHome + File.separator + "bin" + File.separator + "java";
        String classpath = System.getProperty("java.class.path");
        String className = Server.class.getCanonicalName();
 
        ProcessBuilder builder = new ProcessBuilder(javaBin, "-cp", classpath, className);
 
        return builder.start();
    }
}
