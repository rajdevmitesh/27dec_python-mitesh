num1= int(input("Enter a number 1: "))
num2= int(input("Enter a number 2: "))

if num1 == 0 and num2 != 0:
    print("One of the numbers is zero")
    if num1 < num2:
        print("ans is ", num1 - num2)
    if num1 > num2:
        print("ans is ", num1 * num2) 
else:
    print("Number is Zero")
    