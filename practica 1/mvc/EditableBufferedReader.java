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
  			case 1:
  				line.home();
  				break;
  			case 5:
  				line.end();
  				break;
  			/*AIXO ÉS PROVISIONAL: el problema es que no sóc capaç de llegir
  			el botó suprimir, simplement s'hauria de canviar el case per el 			suprimir, actualment el suprimir funciona apretant primer el espai
  			i després el borrar. Per posar un espai s'apreta 2 cops el espai.*/ 
  			case 32:
  				switch(super.read()){
   				 case 32:
   				 	line.addChar((char) ' ');
   				 	break;
  				 case 127:
  				 	line.delete();
  					break;
  				 default:
  					break;
  				}
  				break;
   			//case 21:
  			//	line.delete();
  			//	System.out.print(line.displayString());
  			//	break;
  			case 127:
  				line.backspace();
  				break;
        //Diria que així hauria d'estar bé!!!
			case 27:
			      switch (super.read()) {
				case 91:
				  switch (super.read()) {
				    case 67:
				      line.moveCursor(1);
				      break;
				    case 68:
				      line.moveCursor(-1);
				      break;
				    }
				      break;
				}
			break;
			//insertar?
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
  	}
  	unsetRaw();
  	return line.toString();
  }
}
