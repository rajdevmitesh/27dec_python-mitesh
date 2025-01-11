marks = int(input("Enter your marks for Physics: "))
marks_1 = int(input("Enter your marks for Chemistry: "))
marks_2 = int(input("Enter your marks for MAths: "))
mark_3 = int(input("Enter your marks for Biology: "))

total = marks + marks_1 + marks_2 + mark_3
print ("Your total marks are: ", total)
percentage = (total/400)*100
print("Your percentage is: ", percentage)

if  percentage > 70:
        print ("You have passed with A+ grade")
elif percentage > 60:
        print ("You have passed with A grade")
elif percentage >50:
        print ("You have passed with B grade")
elif percentage > 40:
        print ("You have passed with C grade")
else:
        print ("You have failed") 

