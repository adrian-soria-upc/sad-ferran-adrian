import java.io.*;
import java.util.*;

public class Line {
  private int cursor;
  private StringBuilder stringLine;
  private boolean insert;
  private final PropertyChangeSupport propertychange = new PropertyChangeSupport(this);

  public Line(PropertyChangeListener listener){
 	  stringLine = new StringBuilder();
    propertychange.addPropertyChangeListener(listener);
  }

  public void addChar(char in){
  	stringLine.insert(cursor,in);
  	cursor++;
    pcs.firePropertyChange("display", null, getDisplayString());
  }

  public void home(){
      cursor = 0;
      pcs.firePropertyChange("display", null, getDisplayString());
  }

  public void end(){
 	  cursor = stringLine.length();
    pcs.firePropertyChange("display", null, getDisplayString());
  }

  public void delete(){
	  if(cursor < stringLine.length() - 2){
	  	stringLine.deleteCharAt(cursor);
	  }
    pcs.firePropertyChange("display", null, getDisplayString());
  }

  public void moveCursor(int move){
        //move indica amb +1 o -1 si va a l'esquerra o a la dreta
        //SEGUR QUE HI HA UNA MILLOR SOLUCIÓ
        if (cursor + move >= 0 && cursor + move <= stringLine.length()){
            cursor += move;
        }
      pcs.firePropertyChange("display", null, getDisplayString());
  }

  public void backspace(){
  	if(cursor != 0){
	  	stringLine.deleteCharAt(cursor - 1);
		cursor--;
	 }
    pcs.firePropertyChange("display", null, getDisplayString());
  }

  public void insert(){
    insert = !insert;
    pcs.firePropertyChange("display", null, getDisplayString());
  }

  public String displayString(){
    StringBuilder displayString = new StringBuilder();
    displayString.append('\r');
    displayString.append(stringLine.toString());
    displayString.append(" ");
    displayString.append("\033[");
    displayString.append(1 + stringLine.length() - cursor);
    displayString.append("D");
    return displayString.toString();
  }

  public String toString() {
      //StringBuilder builder = new StringBuilder(stringLine.size());
    	//for(Character ch: stringLine){
      //  	builder.append(ch);
    	//}
    	//return builder.toString();
    return stringLine.toString();
  }
}
