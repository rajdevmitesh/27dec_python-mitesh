class student:
    
    def __init__(self, fullname, age, contactnumber):
        
        self.fullname = fullname
        self.age = age
        self.contactnumber = contactnumber
        
        print("Student Info is Like .......")
        
        
s1 = student("John Doe", 20, 1234567890)
print(s1.fullname, s1.age, s1.contactnumber, "\n")
        
s2 = student("kan villiamsun", 25, 1596321478)
print(s2.fullname, s2.age, s2.contactnumber, "\n")
        
s3 = student("jane smith", 22, 3657891245)
print(s3.fullname, s3.age, s3.contactnumber, "\n")


student_info = {}


student_info[s1.fullname] = f"My Name Is  :{s1.fullname}"
student_info[s1.age] = f"My Age Is :{s1.age}"
student_info[s1.contactnumber] = f"My COntact Number Is : {s1.contactnumber}"

student_info[s2.fullname] = f" My Name Is : {s2.fullname}"
student_info[s2.age] = f"My Age Is : {s2.age}"
student_info[s2.contactnumber] = f"My Contact Number Is : {s2.contactnumber}"

student_info[s3.fullname] = f"My Name Is : {s3.fullname}"
student_info[s3.age] = f"My Age Is : {s3.age}"
student_info[s3.contactnumber] = f"My Contact Number Is : {s3.contactnumber}"

print(student_info)

def library_name(library_name):
    for lst in library_name:
        print(lst)
        
library_name(student_info)

