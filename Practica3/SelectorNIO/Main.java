package SelectorNIO;

public class Main {
    public static void main(String[] args) throws Exception {
        if (args.length > 0 && args[0].equals("server")) {
            Server server = new Server();
            server.listen(server.buffer);
        } else if (args.length > 1 && args[0].equals("client")) {
            Client client = Client.start();
            client.sendMessage(args[1]);
            Client.stop();
        }
    }
}
