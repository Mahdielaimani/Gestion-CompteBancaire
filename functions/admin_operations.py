import pandas as pd

def generate_user_id(data):
   if len(data) == 0:
        return 1
   else:
        max_id = data['USER_ID'].max()
        return int(max_id) + 1

def add_client():
    file_path = r'C:\Users\Mahdi Elaimani\Desktop\Projet Python & Scrum\db.xlsx'
    data = pd.read_excel(file_path)

    name = input("Enter client's name: ")
    email = input("Enter client's email: ")
    amount = float(input("Enter client's amount: "))  
    
    user_id = generate_user_id(data)

    new_client_data = pd.DataFrame({
        'USER_NAME': [name],
        'USER_EMAIL': [email],
        'AMOUNT': [amount],
    })

    updated_data = pd.concat([data, new_client_data], ignore_index=True)

    updated_data.to_excel(file_path, index=False)

    print(f"Client '{name}' has been successfully added with USER_ID: {user_id}.")





def delete_client(name, email):
    file_path = r'C:\Users\Mahdi Elaimani\Desktop\Projet Python & Scrum\db.xlsx'
    data = pd.read_excel(file_path)

    index_to_delete = data[(data['USER_NAME'] == name) & (data['USER_EMAIL'] == email)].index

    if not index_to_delete.empty:
        data.drop(index_to_delete, inplace=True)
        data.reset_index(drop=True, inplace=True)  
        data.to_excel(file_path, index=False)
        print(f"User '{name}' with email '{email}' has been successfully deleted.")
    else:
        print(f"User with name '{name}' and email '{email}' not found.")




def show_clients_data():
    file_path = r'C:\Users\Mahdi Elaimani\Desktop\Projet Python & Scrum\db.xlsx'
    data = pd.read_excel(file_path)
    
    if not data.empty:
        print("All Clients:")
        print(data)
    else:
        print("No clients found.")




