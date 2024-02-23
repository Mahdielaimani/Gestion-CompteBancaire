import pandas as pd

def add_client(client_details):
    file_path = r'C:\Users\Mahdi Elaimani\Desktop\Projet Python & Scrum\db.xlsx'
    data = pd.read_excel(file_path)


    max_user_id = data['USER_ID'].max()

    new_user_id = max_user_id + 1 if pd.notna(max_user_id) else 1

    new_client_data = pd.DataFrame({
        'USER_ID': [new_user_id],
        'USER_NAME': [client_details['name']],
        'AMOUNT': [client_details['amount']],
    })

    updated_data = pd.concat([data, new_client_data], ignore_index=True)

    updated_data.to_excel(file_path, index=False)

    print(f"Client '{client_details['name']}' with ID {new_user_id} has been successfully added.")

new_client_details = {
    'name': 'John Doe',
    'amount': 1000.0,
}

add_client(new_client_details)

def delete_client(client_id):
    file_path = r'C:\Users\Mahdi Elaimani\Desktop\Projet Python & Scrum\db.xlsx'
    data = pd.read_excel(file_path)

    if client_id in data['USER_ID'].values:
        data = data[data['USER_ID'] != client_id]

        data.to_excel(file_path, index=False)
        print(f"Client with ID {client_id} has been successfully deleted.")
    else:
        print(f"Client with ID {client_id} not found in the database.")



import pandas as pd

def display_client_data():
    file_path = r'C:\Users\Mahdi Elaimani\Desktop\Projet Python & Scrum\db.xlsx'
    data = pd.read_excel(file_path)

    print("Client Data:")
    print(data)

