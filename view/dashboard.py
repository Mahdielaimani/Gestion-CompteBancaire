list_operation_client = []

def welcome():
    print("Welcome X to your account. Choose the operation:")
    operation = input("Available operations: op1, op2, op3\n")
    
    operations = {
        'op1': consulter_solde,
        'op2': afficher_historique,
        'op3': afficher_montant
    }

    if operation in operations:
        operations[operation]()
    else:
        print("Invalid operation.")

def consulter_solde():
    print("Consulter le solde")

def afficher_historique():
    print("Afficher l'historique des transactions")

def afficher_montant():
    print("Afficher montant")




