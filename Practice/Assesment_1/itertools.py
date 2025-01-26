from itertools import accumulate
import operator

input_number = int(input("how Many Number You want to add"))
number = []
for i in range(input_number):
    a= int(input("enter a Number"))
    number.append(a)
    print(number)
acc = accumulate(number, operator.mul)
print(number)
print(list(acc))

