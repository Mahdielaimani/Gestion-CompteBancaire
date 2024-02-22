
def sign_up():
    print("Create Account")
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    
    while True:
        password = input("Enter your password: ")
        confirm_password = input("Confirm your password: ")
        if password != confirm_password:
            print("The passwords do not match. Please try again.")
        else:
            print("Account created")
            print("Name:", name)
            print("Email:", email)
            break