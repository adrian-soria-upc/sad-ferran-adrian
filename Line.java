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
  public String toString() {
        StringBuilder builder = new StringBuilder(stringLine.size());
    	for(Character ch: stringLine){
        	builder.append(ch);
    	}
    	return builder.toString();
  }
}
