def consulter_solde():
    print("Consulter le solde")

def afficher_historique():
    print("Afficher l'historique des transactions")

def afficher_montant():
    print("Afficher montant")

def transfer_money():
    print("Afficher montant")

   
  
def dashboard_client():
    print("Available operations:")
    print("1. Consulter le solde")
    print("2. Afficher l'historique des transactions")
    print("3. Afficher montant")
    print("3. Transfert money")
    operations = input("Enter operation key Number: ")
    match operations:
        case "1":
         consulter_solde()
        case "2":
         afficher_historique()
        case "3":
         afficher_montant()
        case "4":
         transfer_money()
        case _:
         print("Invalid operation key.")
import functions.client_operations

   
# def dashboard_client():
#     print("Available operations:")
#     print("1. Consulter le solde")
#     print("2. Afficher l'historique des transactions")
#     print("3. Afficher montant")
#     print("3. Transfert money")
#     operations = input("Enter operation key Number: ")
#     match operations:
#         case "1":
#           functions.client_operations.consulter_solde()
#         case "2":
#           functions.client_operations.afficher_historique()
#         case "3":
#          functions.client_operations.afficher_montant()
#         case "4":
#          functions.client_operations.transfer_money()
#         case _:
#          print("Invalid operation key.")
