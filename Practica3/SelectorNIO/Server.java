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
            Set<SelectionKey> selKeys = selector.selectedKeys();
            Iterator<SelectionKey> iter = selKeys.iterator();
            while (iter.hasNext()) {
                SelectionKey key = iter.next();
                if (key.isAcceptable()) {
                    register(selector, serverSocket);
                }
                if (key.isReadable()) {
                    echo(buffer, key);
                }
                iter.remove();
            }
        }
    }

    private static void echo(ByteBuffer buffer, SelectionKey key) throws IOException {
        SocketChannel client = (SocketChannel) key.channel();
        client.read(buffer);
        if (new String(buffer.array()).trim().equals("POISON_PILL")) {
            client.close();
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
 
}
