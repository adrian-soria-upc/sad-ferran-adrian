import java.io.*;

class EditableBufferedReader extends BufferedReader {
  public EditableBufferedReader(Reader in){
  	super(in);
  }
  
  void setRaw(){
  	String[] cmd = {"/bin/sh", "-c", "stty raw </dev/tty"};
	Runtime.getRuntime().exec(cmd);
  }
  void unsetRaw(){
  	String[] cmd = {"/bin/sh", "-c", "stty cooked </dev/tty"};
	Runtime.getRuntime().exec(cmd);
  }
  int read(){
  	
  	}
  int readLine(){
  	
  	}
  }
