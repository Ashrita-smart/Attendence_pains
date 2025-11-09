#Write a program to determine if a student is allowed to write the exam based on the following conditions:
#If the student has a medical condition, they are allowed.


#If not, check their attendance percentage:


#If attendance greater than 75 → Allowed 
#Else  Not Allowed
medication=input("Does this studdent have medical problems?:")

if medication=="Yes":
    print("Allowed")
else:
    number=int(input("enter the students attendence sheet"))
    print(number)
    if number>75:
        print("Allowed")
    else:
        print("Not allowed")