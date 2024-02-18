import auth.signup

def sign_in():
    yes_or_no = input("Do you already have an account? (Yes or No): ").lower()
    
    if yes_or_no == 'yes':
        email = input("Enter your email: ")
        password = input("Enter your password: ")
    else:
        auth.signup.sign_up()

sign_in()
