import java.util.LinkedList;
import java.util.Queue;

public class Customer {

  public static final int counterNos = 3;
  public static Queue<String> customerQueue = new LinkedList<>();
  private static Queue<String>[] counters;

  public static void main(String[] args) {
    // queue.add(1);
    // queue.add(2);
    // queue.add(3);
    // System.out.println(queue);
    counters = new LinkedList[counterNos];

    for(int i=0; i<counterNos; i++) {
      counters[i] = new LinkedList<>();
    }

    customerArrival("Alice");
    customerArrival("Bob");
    customerArrival("Charlie");
    customerArrival("Diana");
    customerArrival("Diana");
    customerArrival("Diana");
    customerArrival("Diana");
    customerArrival("Diana");
    customerArrival("Diana");
    customerArrival("Diana");
    customerArrival("Diana");
    customerArrival("Diana");
    customerArrival("Diana");
    customerArrival("Diana");
    customerArrival("Diana");
    customerArrival("Diana");
    customerArrival("Diana");

    displayQueue(0); 
    displayQueue(1);
    
    processNext(0);
    displayQueue(0);
  }

  public static void customerArrival(String customerName) {
    int shortestQueue = 0;
    int shortestQueueSize = counters[0].size();

    for (int i = 0; i < counterNos; i++) {
      if(counters[i].size() < shortestQueueSize) {
        shortestQueueSize = counters[i].size();
        shortestQueue = i;
      }
    }
    customerQueue.add(customerName); // add them to shortest queue
    System.out.println(customerName + " joined queue " + shortestQueue);
  }
  public static void processNext(int counterNo) {
    if (counterNo >= 0 && counterNo < counterNos) {
      Queue<String> queue = counters[counterNo];
      if (!queue.isEmpty()) {
        String customerName = queue.poll(); //see first customer in the queue
        System.out.println("Processing Customer at "+customerName+ "at counter "+counterNo);
      } else {
        System.out.println("No customers to process at counter "+counterNo);
      }
    }else {
      System.out.println("Invalid counter number: " +counterNo);
    }
  }
  public static void displayQueue(int counterNo) {
    if (counterNo >= 0 && counterNo < counterNos) {
      System.out.println("Queue at counter " +counterNo+": "+counters[counterNo]);
    } else {
      System.out.println("Invalid counter number: " + counterNo);
    }
  }
}
