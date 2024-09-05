// package stacks;

import java.io.IOException;
import java.util.*;

public class Browser {
  public static String page = "https://www.geeksforgeeks.org/constructor-chaining-java-examples/";
  public static String page2 = "https://www.geeksforgeeks.org/";
  public static String page3 = "https://www.geeksforgeeks.org/arrays-in-java/?ref=shm";
  public static Stack<String> backStack = new Stack<>();
  public static Stack<String> forwardStack = new Stack<>();
  public static String currentPage = null;
  public static void main(String[] args) {
    visit(page);
    visit(page2);
    visit(page3);

    // first go back then forward
    back();
    back();

    forward();

    visit("https://google.com");

    displayCurrentPage();
    displayBackStack();
    displayForwardStack();
  }

  public static void visit(String page) {
      // Runtime.getRuntime().exec(new String[]{"bash", "-c", String.format("google-chrome %s",page)});
      if (currentPage != null) {
        backStack.push(currentPage);
      }
      currentPage = page;
      forwardStack.clear();
      System.out.println("Visited: "+currentPage);
  }

  public static void back() {
    if (!backStack.empty()) {
    forwardStack.push(currentPage);
    currentPage = backStack.pop();
    System.out.println("Back to: "+currentPage);
    } else {
      System.out.println("No more pages in the back history");
    }
  }
  public static void forward() {
    if (!forwardStack.empty()) {
    backStack.push(currentPage);
    currentPage = forwardStack.pop();
    System.out.println("Forward to: "+currentPage);
    } else {
      System.out.println("No more pages in the forward history");
    }
  }
  public static void displayCurrentPage(){
    System.out.println(currentPage);
  }
  public static void displayBackStack(){
    System.out.println(backStack);
  }
  public static void displayForwardStack(){
    System.out.println(forwardStack);
  }
}
