import pandas as pd

def sign_up():
    file_path = 'C:\\Users\\Mahdi Elaimani\\Desktop\\Projet Python & Scrum\\db.xlsx'
    data = pd.read_excel(file_path)

    print("Create Account")
    name = input("Enter your name: ")
    email = input("Enter your email: ")  
    while True:
        password = input("Enter your password: ")
        confirm_password = input("Confirm your password: ")
        if password != confirm_password:
            print("The passwords do not match. Please try again.")
        else:
            new_index = len(data) + 2
            new_row = {'USER_ID': '', 'USER_NAME': name, 'USER_Email': email, 'AMOUNT':0.0,'NB_TRANS': 0,}
            data.loc[new_index] = new_row
            data.to_excel(file_path, index=False)
            print("Account created")
            print("Name:", name)
            print("Email:", email)
            # import view.dashboard_client

            # view.dashboard_client.dashboard_client()
            break

sign_up()

