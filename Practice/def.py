def getdata(id,name):
    print("Id is :",id)
    print("My Name is:",name) 
n = int(input("Enter the number of pair: "))  
student = {}
id_list = []
name_list = []
for i in range(n):
    id_list= int(input("Enter Your Id: "))
    name_list = input("Enter Your Name: ")
    student[id_list] = name_list
    print(student)
print(f"Id is : {id_list} and Name is : {name_list}")

    
getdata(id_list,name_list)
    
    