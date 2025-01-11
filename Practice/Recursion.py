"""""def natural_numbers(n):
    if n == 0:
        return 0
    return n + natural_numbers(n-1)

print(natural_numbers(5))"""



num_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

def list_library(my_list):
    if len(my_list) == 0:
        return 0
    elif len(my_list[1:8]) > 1:
        print(my_list)
    return my_list

list_library(num_list)
print(list_library(num_list))


