def consulter_solde():
    balance = 1000
    print("Your current account balance is:", balance)


def afficher_historique():
    transaction_history = ["Transaction 1: -$100", "Transaction 2: +$500"] 
    print("Transaction History:")
    for transaction in transaction_history:
        print(transaction)


        
def afficher_montant():
    interest_rate = 0.05  
    balance = 1000  
    interest_earned = balance * interest_rate
    print("Interest earned on your account:", interest_earned)



def transfer_money(sender_account, receiver_account, amount):
   
  
    if sender_account['balance'] >= amount:
        sender_account['balance'] -= amount
        receiver_account['balance'] += amount
        print(f"Transfer of ${amount} successful from {sender_account['account_holder']} to {receiver_account['account_holder']}.")
    else:
        print("Insufficient balance for the transfer.")

sender_account = {'account_number': '123456789', 'account_holder': 'Sender', 'balance': 1000.0}
receiver_account = {'account_number': '987654321', 'account_holder': 'Receiver', 'balance': 500.0}
amount = 200.0

transfer_money(sender_account, receiver_account, amount)
