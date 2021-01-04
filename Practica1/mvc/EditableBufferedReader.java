import java.io.*;

public class EditableBufferedReader extends BufferedReader {
  private Line line;
  public EditableBufferedReader(final Reader in){
  	super(in);
  	line = new Line();
  }
  
  private static void setRaw() throws IOException{
  	try{
  		  String[] cmd = {"/bin/sh", "-c", "stty -echo raw </dev/tty"};
		  Runtime.getRuntime().exec(cmd);
	  } catch (IOException e){
		  e.printStackTrace();
	  }
  }

  private static void unsetRaw() throws IOException{
  	try{
  		  String[] cmd = {"/bin/sh", "-c", "stty echo cooked </dev/tty"};
		  Runtime.getRuntime().exec(cmd);
	  } catch (IOException e){
		e.printStackTrace();
	 }
  }

  public int read() throws IOException{
	while(true){
		int command = super.read();
		switch(command){
			case Dict.HOME:
				line.home();
				break;
			case Dict.END:
				line.end();
				break;
			 case Dict.DELETE:
				line.delete();
				break;
			case Dict.BACKSPACE:
				line.backspace();
				break;
		  case Dict.INSERT:
				line.insert();
				break;
		  case Dict.ESC:
				switch (super.read()) {
			  case Dict.CORCHETE:
				switch (super.read()) {
				  case Dict.IZQUIERDA:
					line.moveCursor(1);
					break;
				  case Dict.DERECHA:
					line.moveCursor(-1);
					break;
				  }
					break;
			  }
		  break;
		  default:
			  return command;  	
		}
	}	
}
  
  public String readLine() throws IOException{
  	setRaw();
	int inChar = 0;
  	while((inChar = read()) != Dict.ENTER){
  		line.addChar((char) inChar);
  	}
  	unsetRaw();
  	return line.toString();
  }
}
