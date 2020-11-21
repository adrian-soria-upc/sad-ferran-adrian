/*Programar dues classes MySocket i MyServerSocket que siguin funcionalment equivalents
a les classes de Java Socket i ServerSocket però que encapsu-li’n excepcions i els corresponents
streams de text BufferedReader i PrintWriter. Aquestes classes hauran de disposar de mètodes de 
lectura/escriptura dels tipus bàsics.*/
public class MySocket{
	private final Socket socket;
    private final BufferedReader entrada;
    private final PrintWriter sortida;

    public MySocket(String host, String port){
    	s = new Socket("host", /*Ha de ser un int*/"port");

    	entrada = new BufferedReader(new InputStreamReader(s.getInputStream()));
        sortida = new PrintWriter(s.getOutputStream(), true);


        sendMessage(host);
        sendMessage(port);
    }

     public void sendMessage(final String message) {
        out.println(message);
    }

    public String receiveMessage() throws IOException {
        return in.readLine();
    }
}
