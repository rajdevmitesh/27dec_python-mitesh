data = {}
subject_name1 = input("Enter a First Subject Name: ")
subject_name2 = input("Enter a Second Subject Name: ")
subject_name3 = input("Enter a Third Subject Name: ")

Marks1 = int(input(f" Enter a Marks of :   {subject_name1}  "))
Marks2 = int(input(f" Enter a Marks of :   {subject_name2}  "))
Marks3 = int(input(f" Enter a Marks of :   {subject_name3}  "))

print("Total Marks: ", Marks1 + Marks2 + Marks3)

data[subject_name1] = Marks1
data[subject_name2] = Marks2
data[subject_name3] = Marks3

print(data)