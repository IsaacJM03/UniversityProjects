import java.util.*;
class Payment {
  // Attributes to store worker details
  private String workerName;
  private int daysWorked;
  private double rate;

  // Constructor to initialize the attributes
  public Payment(String workerName, int daysWorked, double rate) {
      this.workerName = workerName;
      this.daysWorked = daysWorked;
      this.rate = rate;
  }

  // Method to calculate the payment
  public double calculatePayment() {
      return daysWorked * rate;
  }

  // Method to display the payment details
  public void displayDetails() {
      System.out.println("Worker Name: " + workerName);
      System.out.println("Days Worked: " + daysWorked);
      System.out.println("Rate: " + rate);
      System.out.println("Payment: " + calculatePayment());
      System.out.println(); // Add an empty line for better formatting
  }
}
public class CalcPayment {

    public static void main(String[] args) {
        Payment[] workers = new Payment[5];

        Scanner scanner = new Scanner(System.in);

        // Get the fixed rate for all workers
        System.out.print("Enter the fixed rate for all workers: ");
        final int rate = scanner.nextInt();

        scanner.nextLine(); // Consume the newline character

        // Get worker details from the user
        for (int i = 0; i < workers.length; i++) {
            System.out.println("Enter details for worker " + (i + 1) + ":");

            System.out.println("Name: ");
            String name = scanner.nextLine();

            System.out.println("Days Worked: ");
            int daysWorked = scanner.nextInt();

            scanner.nextLine(); // Consume the newline character

            workers[i] = new Payment(name, daysWorked, rate);
        }

        // Print payment details for each worker
        for (Payment worker : workers) {
            worker.displayDetails();
        }

        scanner.close(); // Close the scanner to release resources
    }
}