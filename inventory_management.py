# inventory management system using loops

inventory  = {
    "apples": 10,
    "bananas": 5,
    "oranges": 8,
    "grapes": 12,
}

def display_inventory():
    print("\n--Current Inventory--")
    for item, quantity in inventory.items():
        print(f"{item.capitalize()}: {quantity} in stock")
    print("---------------------")
    
def add_item():
    item = input("Enter the item name: ").lower()
    quantity = int(input("Enter the quantity: "))
    if item in inventory:
        inventory[item] += quantity
    else:
        inventory[item] = quantity
    print(f"Added {quantity} {item.capitalize()}(s) to the inventory.")
    
def update_item():
    item = input("Enter the item name to update: ").lower()
    if item in inventory:
        new_quantity = int(input(f"Enter the new quantity for {item.capitalize()}: "))
        inventory[item] = new_quantity
        print(f"Updated {item.capitalize()} quantity to {new_quantity}.")
    else:
        print(f"Item - {item.capitalize()} not found in inventory.")

def main():
    while True:
        print("\n--Inventory Management System--")
        print("Select an option:")
        print("1. Display Inventory")
        print("2. Add Item")
        print("3. Update Item")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            display_inventory()
        elif choice == "2":
            add_item()
        elif choice == "3":
            update_item()
        elif choice == "4":
            print("Exiting the Inventory Management System.")
            break
        else:
            print("Invalid choice. Please try again.")
            
main()