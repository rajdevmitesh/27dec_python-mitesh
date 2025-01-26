name = input("Enter your full name:")
age = input("Enter your age:")
mobile = input("Enter your mobile num:")
email = input("Enter your email:")
pwd = input("Enter your password:")
confirm_pwd = input("Enter your Confirm password:")

if name.isalpha() and age.isdigit() and mobile.isdigit() and email.islower() and pwd.isalnum() and confirm_pwd.isalnum():
    if len(mobile) == 10:
        print("Mobile number is valid")
elif:
    print("your mobile Number is not a 10 digit number or contains alphabets")    
    if pwd == confirm_pwd:
        print("Success")
    else:
        print("Password and Confirm password do not match")
    
else:
    print("Password and Confirm password do not match")