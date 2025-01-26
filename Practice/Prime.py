number = int(input("Enter a number: "))
if number > 1 and number%number == 0 and number/number == number and ((6*number)+1)%2==1  :
    print (f"{number} Is a Prime number")
else:
    print(f"{number} is not a prime number")