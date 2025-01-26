user = {}
k_list = []
val_list = []

n = int(input("Enter number of Pairs: "))
for i in range(n):
    key = input("Enter Key: ")
    k_list.append(key)
    print(key)
    values = []
    value_count = int(input(f"Enter how many key you wanna enter '{key}': "))
    for j in range(value_count):
        val = input("Enter Value: ")
        values.append(val)
        print(val)
    user[key] = values
    print(f"Added {key} with values {values}")

print("Final dictionary:", user)