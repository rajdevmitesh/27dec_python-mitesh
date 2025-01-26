user = {}

n = int(input("Enter number of Pairs: "))
for i in range(n):  
    k_list = [] 
    val_list = []
    key = input("Enter Key: ")
    k_list.append(key)
    print(key)
    values_count = int(input(f"Enter How many times You wanna '{key}': "))
    values = []
    for j in range(values_count):
        val = input("Enter Value: ")
        values.append(val)
        print(val)
        user[key] = values
        print(f"Added {key} with values {values}")
print(user)