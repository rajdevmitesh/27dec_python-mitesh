"""Create a mini-project where students combine conditional statements, loops, and functions
to create a basic Python application, such as a simple calculator or a grade management
system."""

from prettytable import prettytable 

print (" choose if you want to use calculate or use grade management system ")

print("""
    
    Choose 1 For Calculate
    
    Choose 2 for Use grade Management System 
    
    """)

user = int(input("Enter Your number as per ABout instruction "))
print(user)

if user == 1:
    print("You choose for Calculation")

    print('''
        Enter value for addition = add, subtraction = sub, multiplication = mul 
        Division = Div , Modulo = Mol
    ''')
    val = input("Enter the operation you need (): ")
    print("Your Value is :", val)
    
class calculator:
    result = ""
    def operator(self, operator, result):
        self.operator = operator
        self.result = result

    value = ("Enter how many Number You Want to Input")   
    print(value)

    
    #if value
        

if user == 2:
    print("You chose the Grade Management System")
    
print('''

        How Many subject and Student you want to add 
                
    ''')

    #class grade:
class grade:
    
    #  def __init__(self, student_count,):   
           """ def __init__(self, subject, Student):
                self.subject = subject
                self.Student = Student """    

print("Edit Your Student Field........")

#stud_info = {}
total = []
students = []
subjects = []
roll_list = []
name_list= []
subject_count = int(input("Enter the number of Subject: "))
student_count = int(input("Enter the number of students: "))
for j in range(subject_count):
        Subject_name = input("Enter Your Subject name : ")
        print(Subject_name)
        subjects.append(Subject_name)
        print(subjects)
for i in range(student_count):
        name = input("Enter Your name: ")
        name_list.append(name)
        print(name_list)
        roll_no = int(input("Enter Your Roll number: "))
        roll_list.append(roll_no)
        print(roll_list)
for k in range(subject_count): 
        marks = int(input("Enter Your Marks: "))
        print(marks)
        avg = marks / subject_count
        print(avg)
        total.append(marks)
        print(total)
        print("Student Info is Like .......")
for j in range (subject_count):
   """ stud_info [name] = name_list
    stud_info [roll_no] = roll_list
    stud_info [Subject_name] = subjects"""
subject_info = {f" My name Is : {name_list} My roll_no is : {roll_list} My Subject  Is : {subjects} And {subjects}  Marks is : {total}"}
print(subject_info)   
    
for student in students:
    print(student)
        
def print_lists(subject_info):
    for lst in subject_info:
        print(lst)


"""for subject in subjects:
    print(subject)"""
    
    
