import functions.client_operations

def dashboard_client(user_email):
    while True:
        print("Available operations:")
        print("1. Check balance")
        print("2. View transaction history")
        print("3. View amount")
        print("4. Quit the application")
        operation = input("Enter operation key Number: ")

        if operation == "1":
            functions.client_operations.consulter_solde(user_email)
        elif operation == "2":
            functions.client_operations.afficher_historique(user_email)
        elif operation == "3":
            functions.client_operations.afficher_montant(user_email)
        elif operation == "4":
            print("Goodbye! Exiting the application.")
            break
        else:
            print("Invalid operation key.")
