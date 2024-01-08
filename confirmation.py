import json
from email_invoice import generate_invoice_pdf, send_invoice_email

def list_order(order_num):
    order = {}
    with open("order_info.json", "r", encoding="utf-8") as file:
        orders = json.load(file)
    with open("Item_info.json", "r", encoding="utf-8") as file:
        items = json.load(file)
    name, status = "",""
    for code, quantity in orders[order_num].items():
        name = code
        status = quantity
        break
    for code, quantity in orders[order_num].items():
        #print(code)
        #print(quantity)
        if code != name:
            order[code] = [items[code][0][1],quantity,items[code][1][1]]
    return order

def order_name(order_num):
    with open("order_info.json", "r", encoding="utf-8") as file:
        orders = json.load(file)
    name, status = "",""
    for code, quantity in orders[order_num].items():
        name = code
        status = quantity
        break
    return name

def order_status(order_num):
    with open("order_info.json", "r", encoding="utf-8") as file:
        orders = json.load(file)
    name, status = "",""
    for code, quantity in orders[order_num].items():
        name = code
        status = quantity
        break
    return status

def setStatus(order_num, status):
    with open("order_info.json", "r+", encoding="utf-8") as file:
        orders = json.load(file)

        # Check if the order number exists
        if order_num not in orders:
            print(f"Order with number {order_num} not found.")
            return

        # Update the status
        orders[order_num][order_name(order_num)] = status

        # Move the file pointer to the beginning before writing
        file.seek(0)

        # Write the updated orders back to the file
        json.dump(orders, file, ensure_ascii=False, indent=2)

def get_customer_email(customer):
    with open("Customer_info.json", "r", encoding="utf-8") as file:
        customers = json.load(file)
    return customers[customer][0][1]

def calculate_total_price(customer):
    with open("order_info.json", "r", encoding="utf-8") as order_file:
        orders = json.load(order_file)
    
    with open("item_info.json", "r", encoding="utf-8") as item_file:
        items = json.load(item_file)
    total_price = 0
    for code, quantity in orders[customer].items():
        price = items[code][1][1]
        total_price += float(price) * float(quantity)
    return total_price

def main():
    while True:
        num = input("Enter your order number:")
        status = order_status(num)
        if(status == "confirmed payment"):
            print("payment already confirmed")
        else:
            print("Here are your orders:")
            print(list_order(num))
            name = order_name(num)
            confirmation = input("confirm payment?(yse/no)").lower()
            if confirmation =="yes":
                setStatus(num, "confirmed payment")
                invoice_name =f"{name}_Invoice.pdf"
                generate_invoice_pdf(num, name, list_order(num), invoice_name)
                send_invoice_email(name,get_customer_email(name), invoice_name)
        continue_order = input("Continue confirmation?(yes/no)").lower()
        if continue_order != "yes":
            break

if __name__ == "__main__":
    main()