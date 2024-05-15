package Guestjazz;

import java.util.Scanner;

public class NonResident extends Guest {
    private int entranceFee;

    public NonResident(String guestID, String guestName, int numberOfDays, int entranceFee) {
        super(guestID, guestName, numberOfDays);
        this.entranceFee = entranceFee;
    }

    @Override
    public void printDetails() {
        super.printDetails();
        int totalAmount = numberOfDays * entranceFee;
        System.out.println("Entrance Fee per Day: " + entranceFee);
        System.out.println("Total Amount to Pay: " + totalAmount);
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter Guest ID: ");
        String guestID = scanner.nextLine();
        
        System.out.print("Enter Guest Name: ");
        String guestName = scanner.nextLine();
        
        System.out.print("Enter Number of Days: ");
        int numberOfDays = scanner.nextInt();
        
        System.out.print("Enter Entrance Fee per Day: ");
        int entranceFee = scanner.nextInt();

        NonResident nonResident = new NonResident(guestID, guestName, numberOfDays, entranceFee);
        nonResident.printDetails();
    }
}

