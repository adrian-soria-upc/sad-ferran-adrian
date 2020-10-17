import java.io.*;
import java.util.*;

public class Line {
  private int cursor;
  private List<Character> arrayLine;
  public Line(){
 	arrayLine = new ArrayList<Character>();
  }
  public void addChar(char in){
  	arrayLine.add(cursor,in);
  	cursor++;
  }
  public String toString(){
  	return arrayLine.toArray().toString();
  }
}  
