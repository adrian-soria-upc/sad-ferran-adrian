import java.io.*;
import java.util.*;

public class Line {
  private int cursor;
  private ArrayList<Character> stringLine;
  public Line(){
 	stringLine = new ArrayList<Character>();
  }
  public void addChar(char in){
  	stringLine.add(cursor,in);
  	cursor++;
  }
  public void home(){
      cursor=0;
  }
  public void end(){
      cursor=stringLine.size();
  }
  public void delete(){
      stringLine.remove(cursor);
  }
  public void backspace(){
      stringLine.remove(cursor-1);
      cursor--;
  }
  public String toString() {
        StringBuilder builder = new StringBuilder(stringLine.size());
    	for(Character ch: stringLine){
        	builder.append(ch);
    	}
    	return builder.toString();
  }
}
