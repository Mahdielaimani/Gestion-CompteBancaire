import auth.signin_admin
import auth.signin_client

def main():
    print("Welcome To Bank IAV")
    role = input("Are you logging in as an administrator or a client? (admin/client): ").lower()
    if(role == 'admin'):
        auth.signin_admin.sign_in_admin()
    elif (role == 'client'):
        auth.signin_client.sign_in_client()
    else:
        print("Invalid input. Please enter 'admin' or 'client'.")

if __name__ == "__main__":
    main()