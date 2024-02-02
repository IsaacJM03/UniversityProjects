import java.io.*;

public class Student {
  public String RegNumber;
  public int age;
  protected static String College;


public static void main(String[] args)
{
  int x = 10;
  int[] A = {10,20,30,40};
  int [][] b = {{10,20},{30,40}};

  for (int i[]:b) {
    for (int j:i)
      System.out.println(j);
  }

  for (int i = 0; i < A.length;i++)
    System.out.println(i);
  Student s = new Student();
  College = "CoCis";
  // System.out.println("College",College);
}

}

// manipulating matrices, column vectors