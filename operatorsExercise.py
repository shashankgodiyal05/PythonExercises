### Date - 26/12/2022

# 1. Write a program to convert a input meter distance to feet.

meter = float(input("Enter the number in meter to convert it into the feet: "))

feet = meter * 3.2808399
print(meter, "meter is", feet, "in feet.")


# 2. Write a program to convert a input celcius temperature in fahrenheit.

celsius = float(input("Enter the temperature in degree celsius: "))

fahrenheit = celsius * 1.800 + 32.00
print(celsius, "degree censius is", fahrenheit, "in degree fahrenheit.")


# 3. Write a program to calculate the total marks and percentage(out of 300) of student input test marks in English, Maths and Science.

marksEng = float(input("Enter the test marks of English: "))
marksMaths = float(input("Enter the test marks of Maths: "))
marksSci = float(input("Enter the test marks of Science: "))

totalMarks = marksEng + marksMaths + marksSci
percentMarks = totalMarks / 3

print("Total marks obtained:", totalMarks)
print("Percentage marks:", percentMarks, "%")


# 4. Write a program to find an input number is even(result is in True and False).

number1 = int(input("Enter a number to check if it is even or not: "))

print(number1, "is the number you entered,")
print("Is it true that entered number is even:", number1 % 2 == 0)

# 5. Write a program to calculate the area and circumference of a cicle with user input radius.

radius = float(input("Enter the radius of the circle in centimeter: "))
pi = 3.14

areaOfCircle = pi * radius**2
circumference = 2 * pi * radius

print("Area of circle with", radius, "cm radius is", areaOfCircle, "cm^2.")
print("Circumference of circle with", radius, "cm radius is", circumference, "cm")


# 6. Write a program to calculate the area and perimeter of rectangle with user input length and breadth.

length = float(input("Enter the length of the rectangle in cm: "))
breadth = float(input("Enter the breadth of the rectangle in cm: "))

areaOfRectangle = length * breadth
perimeterOfRectangle = 2 * (length + breadth)

print("Area of rectangle with", length, "cm length and", breadth, "cm breadth is", areaOfRectangle, "cm^2")
print("Perimeter of rectangle with", length, "cm length and", breadth, "cm breadth is", perimeterOfRectangle, "cm")
