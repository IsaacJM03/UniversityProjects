public class LinkedListPractice {
  static Node head;

  static class Node {
    int data;
    Node next;

    Node(int d)
    {
      data =  d;
      next = null;
    }
  }

  void removeDuplicates()
  {
    Node pointer1 = null, pointer2 = null, duplicate = null;
    
    pointer1 = head;

    // pick elements one by one
    while (pointer1!=null && pointer1.next != null) {
      pointer2 = pointer1;

      // compare the picked element with the rest
      while(pointer2.next != null) {
        // if duplicate, delete
        if (pointer1.data == pointer2.next.data) {
          pointer2.next = pointer2.next.next;
          System.gc(); //garbage collector to clear memory
        }else {
          pointer2 = pointer2.next;
        }
      }
      pointer1 = pointer1.next;
    }
  }

  void printList(Node node)
  {
      while (node != null) {
          System.out.print(node.data + " ");
          node = node.next;
      }
  }

  public static void main(String[] args) {
    LinkedListPractice list = new LinkedListPractice();
    // list.head = new Node(10);
    // list.head.next = new Node(12);
    // list.head.next.next = new Node(11);
    // list.head.next.next.next = new Node(11);
    // list.head.next.next.next.next = new Node(7);
    // list.head.next.next.next.next.next = new Node(8);
    // list.head.next.next.next.next.next.next = new Node(10);
    list.head = new Node(10);
    list.head.next = new Node(12);
    list.head.next.next = new Node(11);
    list.head.next.next.next = new Node(11);
    list.head.next.next.next.next = new Node(12);
    list.head.next.next.next.next.next = new Node(11);
    list.head.next.next.next.next.next.next
        = new Node(10);

    System.out.println(
        "Linked List before removing duplicates : ");
    list.printList(head);

    list.removeDuplicates();
    System.out.println("\n");
    System.out.println(
        "Linked List after removing duplicates : ");
    list.printList(head);
  }
}