import json
import uuid

def generate_unique_Order_number(prefix="ITEM"):
    # Use a combination of prefix, a unique identifier, and some random characters
    unique_id = str(uuid.uuid4().int)[:12]  # Take the first 12 digits of the UUID
    return f"{unique_id}"

def CheckStorage():
    # Load customer and item information
    with open("Customer_info.json", "r", encoding="utf-8") as file:
        customers = json.load(file)
    with open("Item_info.json", "r", encoding="utf-8") as file:
        items = json.load(file)

    order_lst = {}
    
    # Process each customer's order
    for customer_name, order_data in customers.items():
        order_num = generate_unique_Order_number()
        order_lst[order_num] = {}
        order_lst[order_num][customer_name] = ""
        print(order_data)
        for item, lst in order_data:
            if item == "Order":
                for code, quantity in lst.items():
                    # Check if the item is in stock and has enough quantity
                    if items[code][5][1] == "In stock" and int(items[code][2][1]) >= int(quantity):
                        # Update order list
                        order_lst[order_num][code] = int(quantity)
                        # Update item quantity and status
                        items[code][2][1] = str(int(items[code][2][1]) - int(quantity))
                        if items[code][2][1] == "0":
                            items[code][5][1] = "Out of Stock"
        order_lst[order_num][customer_name] = "Storage Checked"
        if not order_lst[order_num]:
            del order_lst[order_num]


    # Print the updated order list
    print("Updated Order List:", order_lst)

    # Update item information in the "Item_info.json" file
    with open("Item_info.json", "w", encoding="utf-8") as file:
        json.dump(items, file, ensure_ascii=False, indent=2)
    with open("order_info.json", "w", encoding="utf-8") as file:
        json.dump(order_lst, file, ensure_ascii=False, indent=2)

# Call the function to check storage and update information
CheckStorage()
