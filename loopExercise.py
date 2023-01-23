## 1. Check the prime number given from the user

# n1 = int(input("Enter the number: "))
# a = 1
# count1 = 0

# while a <= n1:
#     if n1 % a == 0:
#         count1 += 1

#     a += 1

# if count1 == 2:
#     print(n1, "is a prime number.")

# else:
#     print(n1, "is not a prime number.")


## 2. Accept 'n' number from user and calculate the sum of all number between 1 and 'n' including 'n'

# n2 = int(input("Enter the number: "))
# b = 1
# sum = 0

# while b <= n2:
#     sum += b
#     b += 1

# print("The sum of all the numbers between 1 - 10 is", sum)


## 3. Display numbers which are divisible by 5 and if you find number greater than 150 stop the loop iteration.

# c = 1

# while c <= 150:

#     if c % 5 == 0:
#         print(c)

#     c += 1


## 4. Given a number count the total number of digits in a number.

# 12345 // 10 will remove 5, count += 1 which is 1
# 1234 // 10 will remove 4, count += 1 which is 2
# 123 // 10 will remove 3, count += 1 which is 3
# 12 // 10 will remove 2, count += 1 which is 4
# 1 // 10 will remove 1, count += 1 which is 5

# num1 = 64556984568526
# count = 0

# while num1 > 0:
#     temp1 = num1 % 10
#     # print(temp1)
#     count = count + 1
#     # print(count)
#     num1 //= 10

# print(count)


## 5. Calculate the sum of Natural Numbers.

# d = 0
# sum2 = 0

# while d < 10:
#     sum2 += d
#     d += 1

# print("The sum of all Natural numbers 0 - 9 is", sum2)


## 6. Find the Factorial of a number.

# e = int(input("Enter a number to find its Factorial: "))
# rslt = 1

# while e > 0:
#     rslt *= e
#     print(rslt)
#     e -= 1

# print(rslt)


## 7. Generate Multiplication Table 

# f = 1
# num = 5

# while f <= 10:
#     print(num, "*", f, "=", num * f)
#     f += 1


## 8. Write a Python program to get the Fibonacci series between 0 to 50.
    # note: The Fibonacci Sequence is the series of numbers :
    # 0, 1, 1, 2, 3, 5, 8, 13, 21, ....

# number1 = 0
# number2 = 1

# print(number1, end=", ")

# while number2 < 50:
#     print(number2, end=", ")

#     temp = number1
#     number1 = number2
#     number2 = number1 + temp

# print(end="....")


## 9. Find GCD(Greatest Common Divisor) of two numbers.


    
## 10. Find LCM of two numbers.

# num = int(input("Enter a number to get its GCD:"))
# count = 0
# div = 0

# for x in range(2, num+1):
#     if num % x == 0:
#         div = x
#         break
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# while num > 1:
#     num = num // div
#     print(div, end=" ")


## 11. Display characters from A to Z using loop.

# for x in range(65, 91):
#     print(chr(x))

## 12. Reverse a number.

# l = int(input("Enter a number:"))

# rev = 0

# while l > 0:
#     l1 = l % 10
#     rev = rev * 10 + l1
#     l //= 10
# print("Reverse Number: ", rev)


## 13. Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700(both included).

# g = 1500

# while g <= 2700:

#     if g % 7 == 0 and g % 5 == 0:
#         print(g, end=" ")

#     g += 1


## 14. Write a Python program to guess a number between 1 to 9.
    # Note : User is prompted to enter a guess. If the guesses are wrong then the prompt appears again until the guess is correct, on successful guess, user will get a "Well guessed!" message, and the program will exit.

# guessNo = int(input("Guess the number between 1 to 9:\n"))
# realNo = 5

# while guessNo != realNo:

#     if guessNo == realNo:
#         print("Well guessed!")
#     else:
#         anotherGuess = int(input("Wrong guess! Take another chance:\n"))
#         guessNo = anotherGuess


## 15. Write a Python program to construct the following pattern, using a nested for loop.

# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

# numP = 5

# for i in range(1, numP+1):
    
#     for k in range(1, i+1):
#         print("* ", end="")
    
#     print()

# numP -= 1

# for i in range(numP):
    
#     for j in range(numP - i):
#         print('* ', end='')
    
#     print()


## 17. Write a Python program to count the number of ever and even odd numbers from a series of numbers.
    # Sample numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
    # Expected Output :
    # Number of even numbers : 4
    # Number of odd numbers : 5

# i = 0
# j = 0

# for h in range(1, 10):
    
#     if h % 2 == 0:
#         i += 1

#     else:
#         j += 1

# print("Number of even numbers :", i)
# print("Number of odd numbers :", j)
    

## 18. Write a Python program that prints all the numbers from 0 to 6 execpt 3 and 6.
    # Note : Use 'continue' statement.
    # Expected Output : 0 1 2 4 5

# for k in range(0,6):
#     k += 1

#     if k == 3 or k == 6:
#         continue
#     else:
#         print(k)


## 21. Write a Python program to find numbers between 100 and 400 (both included) where each digit of a number is an even number.
    # The numbers obtained should be printed in a comma-separated sequence.

# for m in range(100, 401):
#     m1 = m

#     while m > 0:
#         m2 = m % 10
        
#         if m2 % 2 != 0:
#             break
    
#         m //= 10

#     else:
#         print(m1, end=" ")