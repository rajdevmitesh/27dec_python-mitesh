num1 = int(input("Enter a number 1: "))
num2 = int(input("Enter a number 2: "))
ans = ""
print("Enter the 1= addition, 2= subtraction, 3= multiplication, 4= division",ans)
ans = int(input("Enter the operation you want to perform: "))
if ans == 1:
    print("ans is ", num1 + num2)
elif ans == 2:
    print("ans is ", num1 - num2)    
elif ans == 3:    
    print("ans is ", num1 * num2)
elif ans == 4:
    print("ans is ", num1 / num2)
else:
    print("Invalid input")    