import pandas as pd
import auth.signup
import view.dashboard_client

def sign_in_client():
    file_path = r'C:\Users\Mahdi Elaimani\Desktop\Projet Python & Scrum\db.xlsx'
    data = pd.read_excel(file_path)
    data.columns = data.columns.str.strip()

    attempts = 0
    yes_or_no = input("Do you already have an account? (Yes or No): ").lower()
    while attempts < 3:
        if yes_or_no == 'yes':
         email = input("Enter your email: ")
         password = input("Enter your password: ")
         if not data[(data['USER_EMAIL'] == email) & (data['USER_Password'] == password)].empty:
            print("You have successfully signed in.")
            view.dashboard_client.dashboard_client(email)
            break
         else:
            print("Invalid email or password. Please try again.")
            attempts += 1
        elif yes_or_no == 'no':
            auth.signup.sign_up()
    
    else:
            print("Invalid input. Please enter 'Yes' or 'No'.")
            attempts += 1

    if attempts == 3:
        print("You have exceeded the maximum number of attempts. Please try again later.")



