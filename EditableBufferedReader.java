import java.io.*;

public class EditableBufferedReader extends BufferedReader {
  private Line line;
  public EditableBufferedReader(final Reader in){
  	super(in);
  	line = new Line();
  }
  
  private static void setRaw() throws IOException{
  	try{
  		String[] cmd = {"/bin/sh", "-c", "stty raw </dev/tty"};
		Runtime.getRuntime().exec(cmd);
	} catch (IOException e){
		e.printStackTrace();
	}
  }
  private static void unsetRaw() throws IOException{
  	try{
  		String[] cmd = {"/bin/sh", "-c", "stty cooked </dev/tty"};
		Runtime.getRuntime().exec(cmd);
	} catch (IOException e){
		e.printStackTrace();
	}
  }
  public int read() throws IOException{
  	while(true){
  		int command = super.read();
  		switch(command){
  			case 1:
  				line.home();
  				break;
  			case 5:
  				line.end();
  				break;
   			case 21:
  				line.delete();
  				break;
  			case 127:
  				line.backspace();
  				break;
  			//27-91-67 derecha
  			//27-91-68 izquierda
			//insertar?
			default:
				return command;  	
  		}
  	}	
  }
  public String readLine() throws IOException{
  	setRaw();
  	while(read()!=13){
  		line.addChar((char)read());
  	}
  	unsetRaw();
  	return line.toString();
  }
}
