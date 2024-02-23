def add_client():
    print("Add a client")

def delete_client():
    print("Delete a client")

def display_client_data():
    print("Display client data")

def dashboard_admin():
    print("Available admin operations:")
    print("1. Add client")
    print("2. Delete client")
    print("3. Display client data")

    admin_operation_key = input("Enter operation Number: ")

    match admin_operation_key:
     case "1":
        add_client()
     case "2":
        delete_client()
     case "3":
        display_client_data()
     case _:
        print("Invalid admin operation key.")
