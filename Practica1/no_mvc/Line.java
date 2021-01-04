import java.io.*;
import java.util.*;

public class Line {
  private int cursor;
  private StringBuilder stringLine;
  private boolean insert;

  public Line(){
 	  stringLine = new StringBuilder();
  }

  public void addChar(char in){
  	stringLine.insert(cursor,in);
  	cursor++;
  }

  public void home(){
      cursor = 0;
  }

  public void end(){
 	cursor = stringLine.length();
  }

  public void delete(){
	  if(cursor < stringLine.length() - 2){
	  	stringLine.deleteCharAt(cursor);
	  }
  }

  public void moveCursor(int move){
        //move indica amb +1 o -1 si va a l'esquerra o a la dreta
        if (cursor + move >= 0 && cursor + move <= stringLine.length()){
            cursor += move;
        }
  }

  public void backspace(){
  	if(cursor != 0){
	  	stringLine.deleteCharAt(cursor - 1);
		cursor--;
	}
  }

  public void insert(){
    insert = !insert;
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
    return stringLine.toString();
  }
}
