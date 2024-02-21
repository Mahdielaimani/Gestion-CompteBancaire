import auth.signup

def sign_in_client():
    yes_or_no = input("Do you already have an account? (Yes or No): ").lower()
    if yes_or_no == 'yes':
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        print("You have successfully signed in.")
    elif yes_or_no == 'no':
        auth.signup.sign_up()
    else:
        print("Invalid input. Please enter 'Yes' or 'No'.")


