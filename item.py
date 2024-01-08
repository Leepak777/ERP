import json
import uuid

# Sample data for four items
items = {
    "123456":[
        ["item","Laptop"],
        ["Price", "1200.00"],
        ["Quantity", "5"],
        ["Description", "High-performance laptop"],
        ["StorageLocation", "Warehouse A"],
        ["Status", "In stock"]
    ],
    "789012":[ 
        ["item","Smartphone"],
        ["Price", "500.00"],
        ["Quantity", "10"],
        ["Description", "Latest smartphone model"],
        ["StorageLocation", "Warehouse B"],
        ["Status", "In stock"]
    ],
    "345678":[
        ["item","Headphones"],
        ["Price", "80.00"],
        ["Quantity", "20"],
        ["Description", "Noise-canceling headphones"],
        ["StorageLocation", "Warehouse C"],
        ["Status", "In stock"]
    ],
    "901234":[
        ["item","Tablet"],
        ["Price", "300.00"],
        ["Quantity", "8"],
        ["Description", "10-inch tablet"],
        ["StorageLocation", "Warehouse A"],
        ["Status", "In stock"]
    ]
}

def generate_unique_barcode(prefix="ITEM"):
    # Use a combination of prefix, a unique identifier, and some random characters
    unique_id = str(uuid.uuid4().int)[:6]  # Take the first 6 digits of the UUID
    return f"{unique_id}"

def get_user_input():
    name = input("Enter item name: ")
    price = input("Enter item price: ")
    quantity = input("Enter Item quantity: ")
    description = input("Enter Item Description: ")
    location = input("Enter Item Storage Location: ")
    status = input("Enter Item status: ")
    
    return name, price, quantity, description, location, status

def save_data_to_file(name, price, quantity, description, location, status):
    barcode = generate_unique_barcode()
    customer = {
        barcode: [
            ["item", name],
            ["Price", price],
            ["Quantity", quantity],
            ["Description", description],
            ["StorageLocation", location],
            ["Status", status]
        ]
    }
    
    json_file_path = 'Item_info.json'
    try:
        # Try to load existing data
        with open(json_file_path, 'r', encoding='utf-8') as json_file:
            existing_data = json.load(json_file)
    except FileNotFoundError:
        existing_data = {}  # If file doesn't exist yet

    # Append the new entry to the existing data
    existing_data.update(customer)

    # Save the updated data back to the file
    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(existing_data, json_file, ensure_ascii=False, indent=2)

def remove_item_by_name_and_code(name, code):
    json_file_path = 'Item_info.json'

    try:
        # Try to load existing data
        with open(json_file_path, 'r', encoding='utf-8') as json_file:
            existing_data = json.load(json_file)
    except FileNotFoundError:
        print(f"Item with name '{name}' and code '{code}' not found.")
        return

    # Check if the item with the specified name and code exists
    if code in existing_data and existing_data[code][0][1] == name:
        del existing_data[code]
        with open(json_file_path, 'w', encoding='utf-8') as json_file:
            json.dump(existing_data, json_file, ensure_ascii=False, indent=2)
        print(f"Item with name '{name}' and code '{code}' removed successfully.")
    else:
        print(f"Item with name '{name}' and code '{code}' not found.")

def main():
    json_file_path = 'Item_info.json'
    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(items, json_file, ensure_ascii=False, indent=2)

    print("Welcome to the data input program!")

    enter = input("Enter item?(yes/no)")
    while enter == "yes":
        user_input = get_user_input()

        save_data_to_file(*user_input)

        another_entry = input("Do you want to enter data for another user? (yes/no): ").lower()
        if another_entry != 'yes':
            break
    
    remove = input("Remove item?(yes/no)")
    while remove =="yes":
        name_to_remove = input("Enter item name to remove: ")
        code_to_remove = input("Enter item code to remove: ")

        remove_item_by_name_and_code(name_to_remove, code_to_remove)

        another_removal = input("Do you want to remove another item? (yes/no): ").lower()
        if another_removal != 'yes':
            break

    print("Data entry completed. Thank you!")

if __name__ == "__main__":
    main()


