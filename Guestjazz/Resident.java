package Guestjazz;

import java.util.Scanner;

public class Resident extends Guest {
    private double roomFee;

    public Resident(String guestID, String guestName, int numberOfDays, double roomFee) {
        super(guestID, guestName, numberOfDays);
        this.roomFee = roomFee;
    }

    @Override
    public void printDetails() {
        super.printDetails();
        double totalAmount = numberOfDays * (roomFee + 30);
        System.out.println("Room Fee per Day: " + roomFee);
        System.out.println("Resident Municipal Fee per Day: 30");
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
        
        System.out.print("Enter Room Fee per Day: ");
        double roomFee = scanner.nextDouble();

        Resident resident = new Resident(guestID, guestName, numberOfDays, roomFee);
        resident.printDetails();
    }
}
