# Question 1: Find the average of three numbers entered by the user.

number_1 = int(input('Enter first number: '))
number_2 = int(input('Enter second number: '))
number_3 = int(input('Enter third number: '))

# Average
average = (number_1 + number_2 + number_3)/3
print("Average of three numbers is:\n" , average)

#Question 2: Compute a person's income tax (in $).

#To compute a person's income tax (in $)
Gross_income = float(input("Enter the gross income:\n"))

#There is a $10000 standard deduction.
Standard_deduction = 10000

No_of_dependents = int(input("Enter the number of dependents:\n"))

#There is a $3000 deduction for each dependent.
Dependent_deduction = 3000

Taxable_income = Gross_income - Standard_deduction - (Dependent_deduction * No_of_dependents)
print("Taxable_income:\n", Taxable_income)

#Tax rate = 20%

Tax = (Taxable_income * 20)/100
print("Tax: \n", Tax)


# Question 3: Store different data types into a list.

SID = int(input("Enter the student id:\n"))
Name = str(input("Enter the student's name:\n"))
Gender = str(input("Enter the gender of the student:\n"))
Course_name = str(input("Enter the name of the course:\n"))
CGPA = float(input("Enter student's cgpa:\n"))

Student_list = ['SID', 'Name', 'Gender', 'Course_name', 'CGPA']
print(Student_list)

Student_Info = [SID, Name, Gender, Course_name, CGPA]
print("\n The list of the student information:\n ",Student_Info)


# Question 4: Enter marks of 5 students into a list and display in a sorted manner

student1_marks = int(input("Enter the marks of student_1:\n "))
student2_marks = int(input("Enter the marks of student_2:\n "))
student3_marks = int(input("Enter the marks of student_3:\n "))
student4_marks = int(input("Enter the marks of student_4:\n "))
student5_marks = int(input("Enter the marks of student_5:\n "))

Student_markslist = [student1_marks, student2_marks, student3_marks, student4_marks, student5_marks]
print("List of student's marks:\n",Student_markslist )

# To display marks in a sorted manner

Student_markslist .sort()

print("Sorted list of student's marks:\n",Student_markslist )


"""
# Question 5: 
        (a) python program to remove 4th element.
        (b) Remove 'Black' and 'Pink' and replace with 'Purple'
"""

Color_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# print (a) part
print('\n(a)')
print(Color_list)
# Removing 4th element of the the list i.e 'Black'
Color_list.remove('Black')
print("\nList after removing 4th element:\n",Color_list)

Color_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# print(b) part
print('\n(b)')
print(Color_list)
# Replacing 'Black' and 'Pink' with 'Purple'
Color_list[3:5] = ["Purple"]
print("\nList after replacing 'Black' and 'Pink' with 'Purple':\n",Color_list)

