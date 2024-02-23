import pandas as pd
import view.dashboard_admin
def sign_in_admin():
    file_path = r'C:\Users\Mahdi Elaimani\Desktop\Projet Python & Scrum\db.xlsx'
    data = pd.read_excel(file_path)

    data.columns = data.columns.str.strip()

    print("Hello Administrator:")
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    if not data[(data['Admin_Email'] == email) & (data['Admin_Password'] == password)].empty:
        print("You have successfully signed in as an administrator.")
        view.dashboard_admin.dashboard_admin()
    else:
        print("Invalid email or password. Please try again.")

