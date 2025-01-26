
# This Python code snippet is creating a simple calculator program that allows the user to perform
# basic arithmetic operations on two numbers.
a = int(input("Enter number 1 :"))
b = int(input("Enter number 2 :"))

while True:
    print("1 Addition :")
    print("2 Subtraction :")
    print("3 Multiplication :")
    print("4 Division")
    print("5 Modulo :")
    print("6 Exit!")
    choice = int(input("Enter your choice(1to6) :"))
    if choice==6:
        break
    match choice :
        case 1 :
            print(a+b)
            
        case 2:
            print(a-b)
            
        case 3:
            print(a*b)
            
        case 4:
            print(a/b)
            
        case 5:
            print(a%b)
            