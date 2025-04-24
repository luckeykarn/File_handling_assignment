import csv
import os
from datetime import datetime, timedelta

inventory_file = "product.csv"
inventory = []

def load_inventory():
    if os.path.exists(inventory_file):
        with open(inventory_file, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) == 3:
                    product = {
                        "name": row[0],
                        "quantity": int(row[1]),
                        "price": float(row[2])
                    }
                    inventory.append(product)

def save_inventory():
    with open(inventory_file, "w", newline="") as file:
        writer = csv.writer(file)
        for product in inventory:
            writer.writerow([product["name"], product["quantity"], product["price"]])

# Load existing inventory on startup
load_inventory()

while True:
    print("\n--- product Manager ---")
    print("1.Addproduct")
    print("2.Updateproductquantity")
    print("3.productlist")
    print("4.Exit")

    choice = input("Choose an option for Inventory management: ")

# add product in inventory
    if choice == "1":
        def add_product():
            name = input("Enter the Product name: ").lower()
            quantity = int(input("Enter How many Products Quantity, wanted to add in innventory: "))
            price = float(input("Enter the Product Price per unit: "))

            product = {
                "name": name,
                "quantity": quantity,
                "price": price
            }

            inventory.append(product)
            save_inventory()
            print(f"{product["name"]} added to inventory successfully!")

        add_product()

# update product quantity in product
    elif choice == "2":
        name = input("Enter the Product name: ").lower()
        quantity = int(input("Enter How many Products Quantity, wanted to add in inventory: "))
        updated = False

        for product in inventory:
            if product["name"] == name:
                print(f"Current Price: {product['price']} per unit")
                new_price = float(input("Enter the new price per unit (or same as current): "))

            
                product["quantity"] += quantity
                product["price"] = new_price
                total_price = product["quantity"] * product["price"]

                updated = True
                break

        if updated:
            save_inventory()
            print(f"{product['name']} | Updated_quantity: {product['quantity']} | Updated_price: {total_price} updated successfully")
        else:
            print("Product not found in inventory.")


# view product list
    elif choice == "3":
        def view_inventory_list():
            found = False
            print("\n--- Product List in the product ---")
            total_value = 0
            for product in inventory:
                print(f"{product['name']} | Quantity: {product['quantity']} | Price: {total_price}")
                total_value += product["quantity"] * product["price"]
                found = True
            if found:
                print(f"Total Inventory Value: {total_value}")
            else:
                print("No products found.")

        view_inventory_list()


    elif choice == "4":
        print("Exiting Inventory Management.")
        break

    else:
        print("Invalid choice. Please select from the menu.")
