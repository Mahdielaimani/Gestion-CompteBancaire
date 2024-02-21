import auth.signin_admin
import auth.signin_client
def sign_in():
    role = input("Are you logging in as an administrator or a client? (admin/client): ").lower()
    if role == 'admin':
        auth.signin_admin.sign_in_admin()
    elif role == 'client':
        auth.signin_client.sign_in_client()
    else:
        print("Invalid input. Please enter 'admin' or 'client'.")

list_operation_client = []

def welcome():
    print("Welcome X to your account. Choose the operation:")
    operation = input("Available operations: op1, op2, op3\n")
    
    # Define operations dictionary
    operations = {
        'op1': consulter_solde,
        'op2': afficher_historique,
        'op3': afficher_montant
    }

    # Execute operation if it exists in the dictionary, otherwise print invalid operation
    if operation in operations:
        operations[operation]()
    else:
        print("Invalid operation.")

# Define functions for each operation
def consulter_solde():
    print("Consulter le solde")

def afficher_historique():
    print("Afficher l'historique des transactions")

def afficher_montant():
    print("Afficher montant")

# Example usage:
welcome()
