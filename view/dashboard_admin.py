
import functions.admin_operations

def dashboard_admin():
    print("Available admin operations:")
    print("1. Add client")
    print("2. Delete client")
    print("3. Display client data")
    admin_operation_key = input("Enter operation Number: ")

    match admin_operation_key:
     case "1":
        functions.admin_operations.add_client()
     case "2":
        name = input("Enter user's name to delete: ")
        email = input("Enter user's email to delete: ")
        functions.admin_operations.delete_client(name, email)
     case "3":
          functions.admin_operations.show_clients_data()
     case _:
        print("Invalid admin operation key.")
