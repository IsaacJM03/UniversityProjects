package CollectionsPractice;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class ArrayListExample {
  public static void main(String[] args) {
    List <String>  fruits = new ArrayList<>();

    fruits.add("orange");
    fruits.add("mango");
    fruits.add("apple");
    fruits.add("pineapple");

    System.out.println("Orig list:" + fruits);

    Collections.sort(fruits); //sorting the list
    System.out.println("Sorted List: "+fruits);

    String firstFruit = fruits.get(0); //get first element
    System.out.println("Fitst fruit is: "+firstFruit);

    fruits.remove("orange");
    System.out.println("List after removing orange: "+fruits);

    // iterating over the list
    for (String fruit : fruits) {
      System.out.println(fruit);
    }
  }
}
