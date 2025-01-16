"""Create a mini-project where students combine conditional statements, loops, and functions
to create a basic Python application, such as a simple calculator or a grade management
system."""


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

        operation = ""
    operation = val
        
arg = " "

def add(arg):
    pass

if user == 2:
    print("You chose the Grade Management System")
    
print('''
                
        How Many subject and Student you want to add 
                
    ''')

print("""Which field you want to edit 

    student  ......


    subject ......


    """)


choice = input("Enter Your choice for edit field")
    
    #class grade:
class grade:
    
    
    #  def __init__(self, student_count,):   
            def __init__(self, subject, Student):
                self.subject = subject
                self.Student = Student         
                
                



if choice == "student":
    print("Edit Your Student Field........")

    # class student
    class student:   
        
        def __init__(self, student_count, name, roll_no):
            self.student_count = student_count
            self.name = name
            self.roll_no = roll_no

            print("Student Info is Like .......")
            
student_count = int(input("Enter the number of students: "))
name = ""
for i in range(student_count):    
            name = input("Enter Your Full name ")
            print("Name Is : ", name)
roll_no = int(input("Enter Your Roll number "))
for j in range(roll_no):
            print("Your Roll No is : ", roll_no)
            print(j)
student_instance = student(student_count, name, roll_no)
print(f"Name: {student_instance.name}, Roll_no: {student_instance.roll_no}")


    # class subject        
class subject:
    
    while choice == "subject":
        pass
    
    print("Edit Your Subject Field........")

        
    def __init__(self, subject, marks):
            self.subject = subject
            self.marks = marks
            print("Subject Info is Like .......")
            print(f"Subject: {self.subject}")
            print(f"Roll_no{self.marks}")

subject_count = int(input("Enter the number of subjects you want to add: "))
print("Your Value is:", subject_count)
    
print("Subject Info is Like .......")


list_sub = []
list_sub.append(subject_count)
print(subject_count)
