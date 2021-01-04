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
  			case 72:
  				line.home();
  				System.out.print(line.displayString());
  				break;
  			case 70:
  				line.end();
  				System.out.print(line.displayString());
  				break;
   			case 51:
  				line.delete();
  				System.out.print(line.displayString());
  				break;
  			case 127:
  				line.backspace();
  				System.out.print(line.displayString());
				  break;
			case 65:
  				line.insert();
  				System.out.print(line.displayString());
  				break;
			case 27:
			      switch (super.read()) {
				case 91:
				  switch (super.read()) {
				    case 67:
				      line.moveCursor(1);
				      System.out.print(line.displayString());
				      break;
				    case 68:
				      line.moveCursor(-1);
				      System.out.print(line.displayString());
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
  	while((inChar = read()) != 13){
  		line.addChar((char) inChar);
  		System.out.print(line.displayString());
  	}
  	unsetRaw();
  	return line.toString();
  }
}
