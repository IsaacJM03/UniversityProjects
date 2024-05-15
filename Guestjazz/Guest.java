package Guestjazz;

public class Guest {
  protected String guestID;
  protected String guestName;
  protected int numberOfDays;

  public Guest(String guestID, String guestName, int numberOfDays) {
      this.guestID = guestID;
      this.guestName = guestName;
      this.numberOfDays = numberOfDays;
  }

  public void printDetails() {
      System.out.println("Guest ID: " + guestID);
      System.out.println("Guest Name: " + guestName);
      System.out.println("Number of Days: " + numberOfDays);
  }
}
