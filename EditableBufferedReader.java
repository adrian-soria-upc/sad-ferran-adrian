import java.io.*;

class TestReadLine {
  void setRaw(){
  	String[] cmd = {"/bin/sh", "-c", "stty raw </dev/tty"};
	Runtime.getRuntime().exec(cmd);
  }
  void unsetRaw(){
  	String[] cmd = {"/bin/sh", "-c", "stty cooked </dev/tty"};
	Runtime.getRuntime().exec(cmd);
  }
  
  public static void main(String[] args) {
    BufferedReader in = new BufferedReader(//new EditableBufferedReader(
      new InputStreamReader(System.in));
    String str = null;
    try {
      str = in.readLine();
    } catch (IOException e) { e.printStackTrace(); }
    System.out.println("\nline is: " + str);
  }
}


