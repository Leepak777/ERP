import json
from storage import CheckStorage

def get_user_input():
    name = input("Enter your name: ")
    email = input("Enter your email address: ")
    b_address = input("Enter your Billing address: ")
    s_address = input("Enter your Shipping address: ")
    C_number = input("Enter your Credit card number: ")
    cvc = input("Enter your CVC: ")
    order = {}
    while True:
        item = input("Enter item barcode: ")
        quantity = input("Enter Quantity: ")
        order[item] = quantity
        new_item = input("New order? (yes/no):").lower()
        if new_item != 'yes':
            break
    return name, email, b_address, s_address, C_number, cvc, order

def save_data_to_file(name, email, b_address, s_address, C_number, cvc, order):
    customer = {}
    customer[name] = [["Email", email], ["Billing Address", b_address], ["Shipping Address", s_address], ["Credit Card Number", C_number], ["CVC", cvc], ["Order", order], ["Confirm", False]]
    json_file_path = 'Customer_info.json'
    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(customer, json_file, ensure_ascii=False, indent=2)

def load_customer_data():
    json_file_path = 'Customer_info.json'

    try:
        with open(json_file_path, 'r', encoding='utf-8') as json_file:
            customer_data = json.load(json_file)
    except FileNotFoundError:
        customer_data = {}

    return customer_data

def save_customer_data(customer_data):
    json_file_path = 'Customer_info.json'

    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(customer_data, json_file, ensure_ascii=False, indent=2)

def edit_user_info():
    customer_data = load_customer_data()

    name_to_edit = input("Enter the name of the user to edit: ")

    if name_to_edit in customer_data:
        print(f"Current information for {name_to_edit}:")
        print(json.dumps(customer_data[name_to_edit], indent=2))

        # Gather updated information
        updated_email = input("Enter updated email address: ")
        updated_b_address = input("Enter updated billing address: ")
        updated_s_address = input("Enter updated shipping address: ")
        updated_C_number = input("Enter updated credit card number: ")
        updated_cvc = input("Enter updated CVC: ")

        # Update user information
        customer_data[name_to_edit][0][1] = updated_email
        customer_data[name_to_edit][1][1] = updated_b_address
        customer_data[name_to_edit][2][1] = updated_s_address
        customer_data[name_to_edit][3][1] = updated_C_number
        customer_data[name_to_edit][4][1] = updated_cvc

        print(f"Information for {name_to_edit} updated successfully.")
    else:
        print(f"User with the name {name_to_edit} not found.")

    save_customer_data(customer_data)
    

def main():
    print("Welcome to the data input program!")

    enter = input("Enter user info?(yes/no)")
    while enter == "yes":
        user_input = get_user_input()

        save_data_to_file(*user_input)

        another_entry = input("Do you want to enter data for another user? (yes/no): ").lower()
        if another_entry != 'yes':
            break
    print("Data entry completed. Thank you!")

    edit = input("Edit user info?(yes/no)")
    while edit == "yes":
        edit_user_info()

        another_edit = input("Do you want to edit information for another user? (yes/no): ").lower()
        if another_edit != 'yes':
            break
    print("User information editing completed. Thank you!")
    
    CheckStorage()

if __name__ == "__main__":
    main()
