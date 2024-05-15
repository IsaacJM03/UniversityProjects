import java.util.Scanner;

public class StudentSACCO {
  private static String regNo;
  private static double balance = 0;

  public static void main(String[] args) {
    Scanner s = new Scanner(System.in);
    System.out.println("Enter Registration Number: ");
    regNo = s.nextLine();

    System.out.println("Enter initial deposit amount: ");
    balance = s.nextDouble();

    while (true) {
      System.out.println("\nMenu:");
      System.out.println("1. Withdraw:");
      System.out.println("2. Deposit:");
      System.out.println("3. Quit");
      System.out.print("Choose an option: ");
      int choice = s.nextInt();

      switch(choice) {
        case 1:
          withdraw(s);
          break;
        case 2:
          deposit(s);
        case 3:
          System.out.println("Exiting the program. Goodbye!");
          System.exit(0);
          break;
        default:
          System.out.println("Invalid option.Please choose again.");
      }
    }
  }

  public static void withdraw(Scanner s)
  {
    System.out.println("Enter amount to withdraw: ");
    double amount = s.nextDouble();

    if (amount <= balance) {
      balance -= amount;
      System.out.println("Withdrawal successful. New balance: "+ balance);
    } else {
      System.out.println("Account " + regNo + " has insufficient funds");
    }
  }

  public static void deposit(Scanner s){
    System.out.print("Enter amount to deposit: ");
    double amount = s.nextDouble();
    balance += amount;
    System.out.println("Deposit successful. New balance: "+ balance);
  }
}