'''
1. Write a Python program to read the age of a candidate and determine whether it is eligible for 
casting his/her own vote. 

Test Data : 21

Expected Output :
Congratulation! You are eligible for casting your vote.
'''

age = int(input("--> Enter your age: "))

if age >= 18:
    print("Congratulation! Your are eligible for casting your vote.")
else:
    print("Your are eligible to cast your vote.")

'''
2. Write a Python program to read the value of an integer m and display the value of n is 1 when m 
is larger than 0, 0 when m is 0 and -1 when m is less than 0. 

Test Data : -5

Expected Output :
The value of n = -1
'''

m = int(input("--> Enter a number: "))

if m == 0:
    n = 0
elif m < 0:
    n = -1
else:
    n = 1

print("The value of n =", n)

'''
## 3. Write a Python program to accept the height of a person in centimeter and categorize the person 
# according to their height. 

# Test Data : 135

# Expected Output :
# The person is Dwarf.
# <140          Dwarf
# >140  <170    Average
# >170         Tall
'''

height = int(input("Enter your height in centimeter: "))

if height < 140:
    print("The person is Dwarf.")
elif height > 140 and height < 170:
    print("The person is Average in height.")
elif height > 170:
    print("The person is Tall.")
else:
    print("Invalid Input !!.")

'''
4. Write a Python program to find the largest of three numbers. 
Test Data : 12 25 52

Expected Output :
1st Number = 12, 2nd Number = 25, 3rd Number = 52
The 3rd Number is the greatest among three
'''

number_1st = int(input("Enter the first no.: "))
number_2nd = int(input("Enter the second no.: "))
number_3rd = int(input("Enter the third no.: "))

print("1st Number =", number_1st, "\t2nd Number =", number_2nd, "\t3rd Number =", number_3rd)

if (number_1st >= number_2nd) and (number_1st >= number_3rd):
    print("The 1st Number is greatest among three")
elif (number_2nd >= number_1st) and (number_2nd >= number_3rd):
    print("The 2nd Number is the greatest among three")
else:
    print("The 3rd Number is the greatest among three")

'''
5. Write a Python program to accept a coordinate point in a XY coordinate system and determine in 
which quadrant the coordinate point lies. 

Test Data : 7 9

Expected Output :
The coordinate point (7,9) lies in the First quadrant.
'''

x = int(input("Enter the first coordinate point: "))
y = int(input("Enter the second coordinate point: "))

if x > 0 and y > 0:
    # first quadrant (positive integer, positive integer)
    print("The coordinate point (", x, ",", y, ") lies in the First quadrant.")

elif x < 0 and y > 0:
    # second quadrant (negetive integer, positive integer)
    print("The coordinate point (", x, ",", y, ") lies in the Second quadrant.")

elif x < 0 and y < 0:
    # third quadrant (negetive integer, negetive integer)
    print("The coordinate point (", x, ",", y, ") lies in the Third quadrant.")

elif x > 0 and y < 0:
    # fourth quadrant (positive integer, negetive integer)
    print("The coordinate point (", x, ",", y, ") lies in the Fourth quadrant.")

else:
    print("These coordinate lies on the x or y axis line or on origin.")

#(1, 0), (-1, 0), (0, 2) and (0, -5) do not lie on any of the four quadrants. They lie on the x-axis 
# or y-axis. (1, 0) and (-1, 0) lie on the x-axis. (0, 0) lies on exactly on Origin


'''
6. Write a python program to find the eligibility
'''




'''
8. Write a Python program to read roll no, name and marks of three subjects and calculate the total, 
percentage and division. 

Test Data :
Input the Roll Number of the student :784
Input the Name of the Student :James
Input the marks of Physics, Chemistry and Computer Application : 70 80 90

Expected Output :
Roll No : 784
Name of Student : James
Marks in Physics : 70
Marks in Chemistry : 80
Marks in Computer Application : 90
Total Marks = 240
Percentage = 80.00
Division = First
'''

rollNo = int(input("-->Enter the roll no.: "))
name = input("-->Enter the name of the student: ")
marksPhy = int(input("-->Enter the marks in Physics: "))
marksChem = int(input("-->Enter the marks in Chemitry: "))
marksCompAppl = int(input("-->Enter the marks in Computer Application: "))

print("\n")

print("Roll No :", rollNo)
print("Name of Student :", name)
print("Marks in Physics :", marksPhy)
print("Marks in Chemistry :", marksChem)
print("Marks in Computer Application :", marksCompAppl)

totalMarks = marksPhy + marksChem + marksCompAppl
print("Total Marks =", totalMarks)

percentage = totalMarks / 3
print("Percentage =", percentage)

if percentage >= 80:
    print("Division = First")

elif percentage >= 60 and percentage < 80:
    print("Division = Second")

elif percentage >= 40 and percentage < 60:
    print("Division = Third")

else:
    print("Fail")

'''
9. Write a Python program to read temperature in centigrade and display a suitable message according
to temperature state below : 

Temp < 0 then Freezing weather
Temp 0-10 then Very Cold weather
Temp 10-20 then Cold weather
Temp 20-30 then Normal in Temp
Temp 30-40 then Its Hot
Temp >=40 then Its Very Hot

Test Data :
42

Expected Output :
Its very hot.
'''

temprature = float(input("-->Enter the temprature in centigrade: "))

if temprature < 0:
    print("Freezing weather.")

elif temprature > 0 and temprature <= 10:
    print("Very cold weather.")

elif temprature > 10 and temprature <= 20:
    print("Cold weather.")

elif temprature > 20 and temprature <= 30:
    print("Normal Temprature.")

elif temprature > 30 and temprature <= 40:
    print("Its Hot.")

elif temprature >= 40:
    print("Its very Hot.")

'''
10. Write a Python program to check whether a triangle is Equilateral, Isosceles or Scalene. 

Test Data :
50 50 60

Expected Output :
This is an isosceles triangle.
'''

sideOne = float(input("Enter the three side of the triangle: "))
sideTwo = float(input())
sideThree = float(input())

if sideOne == sideTwo and sideTwo == sideThree:
    print("Triangle is Equilateral.")

elif sideOne == sideTwo or sideTwo == sideThree or sideOne == sideThree:
    print("Triangle is Isosceles.")

else:
    print("Triangle is Scalene.")

'''
11. Write a Python program to check whether a triangle can be formed by the given value for the angles. 
Test Data :
40 55 65
Expected Output :
The triangle is not valid.
'''

a = int(input("Enter the three angles of triangle: "))
b = int(input())
c = int(input())

if a+b+c==180 and a!=0 and b!=0 and c!=0:
    print("The triangle is valid.")
else:
    print("The triangle is not valid.")

'''
12. Write a Python program to check whether a character is an alphabet, digit or special character. 
Test Data :
@
Expected Output :
This is a special character.

'''

n = input("Enter any character:")
# print(ord(n)) will the print the ascii value of the character as output

if (ord(n) >= 65 and ord(n) <= 90) or (ord(n) >= 97 and ord(n) <= 122):
    print("Alphabet")

elif (ord(n) >= 48 and ord(n) <= 57):
    print("Numeric")

else:
    print("Special character")

'''
13. Write a Python program to check whether an alphabet is a vowel or consonant. 
Test Data :
k

Expected Output :
The alphabet is a consonant.
'''

ch = input("--> Enter an Alphabet: ")

if ch >= 'a' and ch <= 'z':

    if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
        print("Input is vowel.")
    else:
        print("Input is consonant.")

else:
    print("!Invalid Input.")    

'''
15. Write a program in Python to calculate and print the Electricity bill of a given customer. The 
customer id., name and unit consumed by the user should be taken from the keyboard and display the 
total amount to pay to the customer. The charge are as follow :

  +-------------------------------------+-----------------+
  |                Unit                 |    Charge/unit  |
  +-------------------------------------+-----------------+
  |   upto 199	                        |      @1.20      |
  |   200 and above but less than 400   |      @1.50      |
  |   400 and above but less than 600   |      @1.80      |
  |   600 and above	                    |      @2.00      |
  +-------------------------------------+-----------------+

If bill exceeds Rs. 400 then a surcharge of 15% will be charged and the minimum bill should be of Rs. 100/-
Test Data :
1001
James
800

Expected Output :
Customer IDNO :1001
Customer Name :James
unit Consumed :800
Amount Charges @Rs. 2.00 per unit : 1600.00
Surchage Amount : 240.00
Net Amount Paid By the Customer : 1840.00
'''



