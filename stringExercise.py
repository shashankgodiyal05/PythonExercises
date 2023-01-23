# 1. Write a Python program to calculate the length of a string.

# string1 = "Python"

# print(len(string1))
# # this will result- 6


# 2. Write a Python program to check whether an alphabet is a vowel or consonant.

# ch = input("--> Enter an Alphabet: ")

# if ch >= 'a' and ch <= 'z':

#     if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
#         print("Input is vowel.")
#     else:
#         print("Input is consonant.")

# else:
#     print("!Invalid Input.")    


# 3. Write a Python script that takes input from the user and displays that input back in upper and lower cases.

# string2 = input("Enter a Sentence: ")

# print("In lower case: ", string2.lower())
# print("In upper case: ", string2.upper())


# 4. Write a Python program to check number of vowels, consonants and digits and white spaces from a user input string

# st = str(input("Enter a string to count the numbers of vowels, consonants, digits and white spaces of it :"))
# vCount = 0
# cCount = 0
# wsCount = 0
# dCount = 0

# for x in st:
    
#     if x >= 'a' and x <= 'z' or x >= 'A' and x <= 'Z':

#         if x == "a" or x == "e" or x == "i" or x == "o" or x == "u":
#             vCount += 1
#         else:
#             cCount += 1

#     elif x == " ":
#             wsCount += 1

#     elif ord(x) >= 48 or ord(x) <= 57:

#         dCount += 1

# print("Number of vowels in given string:", vCount)
# print("Number of Consonent in given string:", cCount)
# print("Number of white spaces in given string:", wsCount)
# print("Number of digits in given string:", dCount)


# 5. Write a Python program to find the frequency of characters in a string

# string3 = " Python is the best programming language in world. "

# print(string3.count('g'))
# # this will result- 4


# 6. Write a Python program to remove spaces from a given string.

# string6 = " Python is the best programming language in world. "
# print(string6.replace(" ",""))
# # this will result- Pythonisthebestprogramminglanguageinworld


# 7. Write a Python to capitalize first and last letters of each word of a given string.

# string4 = " Python is the best programming language in world. "
# print(string4.title())
# # this will result-  Python Is The Best Programming Language In World. 


# 8. Write a Python program to swap cases of a given string.

# string5 = " Python Is The Best Programming Language In World. "
# print(string5.swapcase())
# # this will result- pYTHON iS tHE bEST pROGRAMMING lANGUAGE iN wORLD.

st = "mera naam sinchan hai, me shararat se bhara, badi mushkil me padi, meri family naohara."

li = st.split()
print(li)