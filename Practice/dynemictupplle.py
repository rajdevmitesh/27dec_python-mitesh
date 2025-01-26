data = []
user = int(input("Enter a Number you want"))

for i in range(user):
    tup = input("Enter a City Name")
    data.append(tup)
print(tuple(data))    