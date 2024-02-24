import pandas as pd

def consulter_solde(user_email):
    file_path = r'C:\Users\Mahdi Elaimani\Desktop\Projet Python & Scrum\db.xlsx'
    data = pd.read_excel(file_path)
    
    user_row = data[data['USER_EMAIL'] == user_email]
    
    if not user_row.empty:
        solde = user_row['AMOUNT'].values[0]
        print(f"Solde for {user_email}: {solde}")
    else:
        print(f"User with email '{user_email}' not found.")

def afficher_historique(user_email):
    file_path = r'C:\Users\Mahdi Elaimani\Desktop\Projet Python & Scrum\db.xlsx'
    data = pd.read_excel(file_path)
    
    user_row = data[data['USER_EMAIL'] == user_email]
    
    if not user_row.empty:
        transaction_history = user_row['NB_TRANS'].values[0]
        print(f"Transaction history for {user_email}: {transaction_history}")
    else:
        print(f"User with email '{user_email}' not found.")

def afficher_montant(user_email):
    file_path = r'C:\Users\Mahdi Elaimani\Desktop\Projet Python & Scrum\db.xlsx'
    data = pd.read_excel(file_path)
    
    user_row = data[data['USER_EMAIL'] == user_email]
    
    if not user_row.empty:
        montant = user_row['AMOUNT'].values[0]
        print(f"Montant for {user_email}: {montant}")
    else:
        print(f"User with email '{user_email}' not found.")
