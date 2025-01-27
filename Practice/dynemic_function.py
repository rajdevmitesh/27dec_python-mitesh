student = {}
def getdata(id,name):
    print("Id is :",id)
    print("My Name is:",name) 
n = int(input("Enter the number of pair: "))  
id_list = []
name_list = []
for i in range(n):
    a = int(input("Enter Your Id: "))
    id_list.append(a)
    print(a)
    b = input("Enter Your Name: ")
    name_list.append(b)
    print(b)
    student[a] = b
print(student)


getdata(id_list,name_list)

