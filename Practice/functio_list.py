# Create a function that will take a list as an argument and return the list.

total_list = []

num_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
alpha_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p']
city_list = ['Karachi','Lahore','Islamabad']
boyname_list = ['Ali','Ahmed','Bilal','Kamran','Noman']
city_list = ['Karachi','Lahore','Islamabad']


print(f'''My Total list is : {num_list} 
    {alpha_list} 
    {city_list} 
    {boyname_list} 
    {city_list}''')

def list_library(my_list):
    
    total_list.append(num_list)
    total_list.append(alpha_list)
    total_list.append(city_list)
    total_list.append(boyname_list)
    total_list.append(city_list)
    
    list = my_list
    print(len(list))
    print(list)
    #return list

    
list_library(total_list)
def print_lists(lists):
    for lst in lists:
        print(lst)

print_lists(total_list)
    
    
    
    

    
    
    