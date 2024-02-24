import functions.admin_operations

def dashboard_admin():
    while True:
        print("Available admin operations:")
        print("1. Add client")
        print("2. Delete client")
        print("3. Display client data")
        print("4. Quit the application")
        admin_operation_key = input("Enter operation Number: ")

        if admin_operation_key == "1":
            functions.admin_operations.add_client()
        elif admin_operation_key == "2":
            name = input("Enter user's name to delete: ")
            email = input("Enter user's email to delete: ")
            functions.admin_operations.delete_client(name, email)
        elif admin_operation_key == "3":
            functions.admin_operations.show_clients_data()
        elif admin_operation_key == "4":
            print("Goodbye! Exiting the application.")
            break
        else:
            print("Invalid admin operation key.")