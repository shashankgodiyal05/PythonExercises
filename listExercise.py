import random

'''
1. Write a Python program to sum all the items in a list.
'''

# li1 = [58, 47, 66, 27, 85, 88]
# sum = 0

# for x in li1:
#     sum += x

# print(sum)

'''
2. Write a python program to multiplies all the items in a list.
'''

# li2 =  [58, 47, 66, 27, 85, 88]
# print(li2 * 4)

'''
3. Write a python program to get the largest number from a list.
'''

# li3 = [58, 47, 66, 27, 85, 88]
# print(max(li3))

'''
4. Write a python program to get the smallest number from a list.
'''

# li4 = [58, 47, 66, 27, 85, 88]
# print(min(li4))

'''
5. Write a python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.
Sample List: ['abc', 'xyz', 'aba', '1221']
Expecter Result: 2 
'''

# li5 = ['abc', 'xyz', 'aba', '1221']
# count5 = 0

# for x in li5:
#     word = str(x)
    
#     if len(word) >= 2:
#         word_len = len(word)

#         if word[0] == word[word_len - 1]:
#             # print(word)
#             count5 += 1

# print(count5)

'''
6. Write a python program to remove duplicates from a list.
'''

# li6 = [58, 47, 66, 66, 27, 27, 85, 88]

# li6_1 = set(li6)
# print(list(li6_1))

'''
7. Write a python program to check a list is empty or not.
'''

# li7 = []

# if len(li7) == 0:
#     print("List is empty.")

# else:
#     print("List is not empty.")

'''
8. Write a python progam to clone or copy a list.
'''

# li8 = [58, 47, 66, 27, 85, 88]
# li8_1 = li8.copy()
# print(li8_1)

'''
9. Write a python program to find the list of words that are longer than n from a given list of words.
'''

# li9_1 = ["mera", "naam", "sinchan", "hai", "me", "shararat", "se", "bhara", "badi", "mushkil", "me", "padi", "meri", "family", "nohara"]
# li9_2 = []

# for x in li9_1:
    
#     if len(x) > 4:
#         li9_2.append(x)

# print(li9_2)

'''
10. Write a python that takes two lists and returns True if they have at least one common member.
'''

# li10 = [58, 47, 66, 27, 85, 88]
# li10_1 = [51, 40, 68, 25, 85, 78]
# count10 = 0

# for x in li10:

#     for y in li10_1:

#         if x == y:
#             count10 += 1

# if count10 == 0:
#     print("Two lists dont have any common member.")
# else:
#     print("Two lists have one or more common members.")

'''
11. Write a python program to print a specified list after removing the 0th, 4th, and 5th elements.
Sample list:- ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
Expected list:- ['Green', 'White', 'Black']
'''

# li11 = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

# li11.pop(5)
# li11.pop(4)
# li11.pop(0)

# print(li11)

'''
12. Write a python program to generate a 3*4*6 3D array whose each element is *. 
'''

# li12 = []
# for x in range(3):

#     li12_1 = []
#     for y in range(4):

#         li12_2 = []
#         for z in range(6):

#             li12_2.append("*")
#         li12_1.append(li12_2)
#     li12.append(li12_1)
# print(li12)

'''
13. Write a python program to print the numbers of a specified list after removing even numbers from it.
'''

# li13 = [58, 47, 66, 27, 85, 88]

# for x in li13:
#     if x % 2 == 0:
#         li13.remove(x)

# print(li13)

'''
14. Write a program to shuffle and print a specific list.
'''

# li14 = ['a', 'b', 'c', 'd', 'e']
# print(random.choices(li14, k=5))

'''
15. Write a program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30(both inclueded).
'''

# li15 = []

# for x in range(1, 6):
#     li15.append(x ** 2)
    
# for y in range(26, 31):
#     li15.append(y ** 2)
    
# print(li15)

'''
16. Write a python program to generate and print a list except for the first 5 elements, where the values are square of numbers between 1 and 30(both included).
'''

# li16 = []

# for x in range(6,31):

#     li16.append(x ** 2)

# print(li16)


'''
17. Write a python program to get the difference between the two lists.
'''

# li17 = [58, 47, 66, 27, 85, 88]
# li17_1 = [58, 47, 66, 27, 85, 88, 58, 54 , 74, 858]
# li17_2 = []

# for x in li17_1:
#     if x not in li17:
#         li17_2.append(x)

# print(li17_2)

'''
18. Write a python program to access the index of a list.
'''

# li18 = [58, 47, 66, 27, 85, 88]
# x = 0

# while x < len(li18):
#     print(li18[x])
#     x += 1

'''
19. Write a python program to convert a list of characters into a string.
'''

# li19 = ['python', 'programming', 66, 27, 85, 88]

# for x in li19:
#     print(str(x))

'''
20. Write a python program to find the index of an item in a specified list.
'''

# li20 = [58, 47, 66, 27, 85, 88]
# print(li20.index(66))

'''
21. Write a python program to flatten a shallow list.
'''

# li21 = [[1, 2, 3], [4, 5, 6]]
# li21_1 = []

# for x in li21:

#     for y in x:
#         li21_1.append(y)

# print(li21_1)

'''
22. Write a python program to append a list to the second list.
'''

# li22 = [58, 47, 66, 27, 85, 88]
# li22_1 = [45, 26, 80, 10]

# print(li22)

# li22 += li22_1
# print(li22)

'''
23. Write a python program to select an item randomly from a list.
'''

# li23 = ["mera", "naam", "sinchan", "hai", "me", "shararat", "se", "bhara", "badi", "mushkil", "me", "padi", "meri", "family", "nohara"]
# print(random.choice(li23))

'''
24. Write a python program to check whether two lists are circularly identical.
'''



'''
25. Write a python program to find the second smallest number in a list.
'''

# li25 = [58, 47, 66, 27, 85, 88]

# li25_1 = li25.copy()

# li25_1.remove(min(li25_1))

# print(min(li25_1))

'''
26. Write a python program to find the second largest number in a list.
'''

# li26 = [58, 47, 66, 27, 85, 88]

# li26_1 = li26.copy()

# li26_1.remove(max(li26_1))

# print(max(li26_1))

'''
27. Write a python program to get unique values from a list.
'''

# li27 = [47, 66, 66, 27, 27, 85, 88]

# li27_1 = set(li27)
# print(list(li27_1))

'''
28. Write a python program to get the frequency of the elements in a list.
'''

# li28 = [47, 66, 66, 27, 27, 85, 88]

# for x in li28:
#     print("Frequency of", x , "=", li28.count(x))

'''
29. Write a python program to count the number of elements in a list within a sprcified range.
'''

# li29 = [47, 66, 66, 27, 27, 85, 88]
# print(len(li29))

'''
30. Write a python program to check whether a list contains a sublist.
'''

# li30 = [[4, 5, 6, 7], 45, 2, [34, 9], "python"]
# count = 0

# for x in li30:
#     if isinstance(x, list):
#         count += 1

# if count != 0:
#     print("This list contains a sublist.")

'''
31. Write a python program to generate all sublists of a list.
'''

# li = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]]

# for x in li:
#     print(x)

'''
32. Write a python program to create a list by concatenating a given list which range goes from 1 to n.
Sample list : ['p', 'q']
n =5
Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']
'''

# li32_1 = ['p', 'q']
# li32_2 = []
# n32 = 5
# # n32 = int(input("Enter a number: "))
 
# for y in range(1, (n32 + 1)):
#     for x in li32_1:
#         z = str(x) + str(y)
#         li32_2.append(z)

# print(li32_2)

'''
33. Write a python program to get varible unique identification number or string.
'''



'''
34. Write a python a program to find common items from two list.
'''

# li34 = [47, 66, 66, 27, 27, 85, 88]
# li34_1 = [458, 686, 66, 237, 271, 805, 88, 88]

# for x in li34:

#     if x in li34_1:
#         print(x)

'''
35. Write a python program to change the position of every n-th value with the (n + 1)th in a list.
Sample list: [0, 1, 2, 3, 4, 5]
Expected Output: [1, 0, 3, 2, 5, 4]
'''



'''
36. Write a python program to convert a list of multiple integers into a single integer.
Sample list: [11, 33, 50]
Expected Output: 113350
'''

# li36 = [11, 33, 50]

# for x in li36:
#     print(x, end="")

'''
37. Write a python program to split a list based on first character of word.
'''

# li37 = ["mera", "naam", "Sinchan", "hai", "me", "shararat", "se", "bhara", "badi", "mushkil", "me", "padi", "meri", "family", "Nohara"]
# li37_m = []
# li37_s = []

# for x in li37:
#     if x[0] == "m":
#         li37_m.append(x)

#     elif x[0] == "s" or x[0] == "S":
#         li37_s.append(x)

# print(li37)
# print(li37_m)
# print(li37_s)

'''
38. Write a python program to create a multiple lists.
'''



'''
39. Write a python program to find missing and additionl values in two lists.
Sample data : Missing values in second list: b,a,c
Additional values in second list: g,h
'''

# li39 = ['a', 'b', 'c', 'd', 'e']
# li39_1 = ['c', 'd', 'e', 'f', 'g', 'h', 'i']

# x_not_in_li39_1 = []
# y_not_in_li39 = []

# for x in li39:
#     if x not in li39_1:
#         x_not_in_li39_1.append(x)

# print("Missing values in second list:", x_not_in_li39_1)

# for y in li39_1:
#     if y not in li39:
#         y_not_in_li39.append(y)

# print("Additional values in second list:", y_not_in_li39)

'''
40. Write a python program to split a list into different variables.
'''

# li40 = [458, 686, 66, 237, 271, 805]

# liVar_0 = li40[0]
# print(liVar_0)

# liVar_1 = li40[1]
# print(liVar_1)

# liVar_2 = li40[2]
# print(liVar_2)

# liVar_3 = li40[3]
# print(liVar_3)

# liVar_4 = li40[4]
# print(liVar_4)

# liVar_5 = li40[5]
# print(liVar_5)

'''
# 42. Write a python program to generate groups of five consecutive numbers in a list.
'''

# li42 =[]

# for x in range(7,17,2):
#     li42.append(x)

# print(li42)

'''
# 43. Write a python program to convert a pair of values into a sorted unique array.
'''

# li43 = [458, 686, 66, 237, 271, 805, 88, 88]

# li43_1 = set(li43)
# li43 = list(li43_1)
# li43.sort()
# print(li43)

'''
44. Write a python program to select the odd items of a list.
'''

# li44 = [458, 686, 66, 237, 271, 805, 88, 88]

# li44_1 = set(li44)
# li44 = list(li44_1)
# li44.sort()

# for x in li44:
#     if x % 2 == 0:
#         li44.remove(x)

# print(li44)

'''
45. Write a python program to insert an element before each element of a list.
'''

# [1, a, 2, b, 3, c, 4, d, 5, e, 6, f, 7, g]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# li45 = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# print(li45)

# for x in range(0, +2):
#     li45.insert(x, str(x))
# ---------------------------------------------------------
# ---------------------------------------------------------
# print(li45)

'''
46. Write a python program to print a nested lists (each list on a new line) using the print() function.
'''

# li46 = [["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000", "#FFFF00"]]

# for x in li46:
#     print(x)

'''
47. Write a Python program to convert list to list of dictionaries. 
Sample lists: ["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000", "#FFFF00"]
Expected Output: [{'color_name': 'Black', 'color_code': '#000000'}, {'color_name': 'Red', 'color_code': '#FF0000'}, {'color_name': 'Maroon', 'color_code': '#800000'}, {'color_name': 'Yellow', 'color_code': '#FFFF00'}]
'''



'''
48. Write a python program to sort a ilst of nested dictionaries.
'''

# li48_1 = [[3, 46, 8, 2, 98, 46, 2], [12, 36, 98, 3, 6, 123, 985], [23, 8]]

# for x in li48_1:
#     for y in x:
#         x.sort()

# print(li48_1)

'''
49. Write a python program to split a list every Nth element.
Sample list: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
Expected Output: [['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]
'''



'''
50. Write a Python program to compute the difference between two lists. 
Sample data: ["red", "orange", "green", "blue", "white"], ["black", "yellow", "green", "blue"]
Expected Output:
Color1-Color2: ['white', 'orange', 'red']
Color2-Color1: ['black', 'yellow']
 '''

# Color1 = ["red", "orange", "green", "blue", "white"]
# Color2 = ["black", "yellow", "green", "blue"]

# print("Color1 - Color2: [ ", end="")
# for x in Color1:

#     if x not in Color2:
#         print(x, end=" ")

# print("]")

# print("Color2 - Color1: [ ", end="")
# for x in Color2:

#     if x not in Color1:
#         print(x, end=" ")

# print("]")

'''
51. Write a python program to create a list with infinite elements.
'''



'''
52. Write a python program to concatenate elements of a list.
'''

# li52 = [458, 686, 66, 237, 271, 805, 88, 88]

# li52 += [55, 43, 65]

# print(li52)

'''
53. Write a python program to remove key values pairs from a list of dictionaries.
'''




'''
54. Write a python program to convert a string to a list.
'''

# string54 = "mera naam sinchan hai"
# print(string54.split())

'''
55. Write a python program to check whether all items of a list is equal to a given string.
'''

# li55 = ['mera', 'naam', 'sinchan', 'hai', 'me', 'sararat', 'se', 'bhara', 'badi', 'muskhkil', 'me', 'padi', 'meri', 'family', 'nohara']

# li55_1 = ['ram', 'ram', 'ram', 'ram', 'ram']
# count = 0

# for x in li55_1:
#     if x == 'ram':
#         count += 1

# if count == len(li55_1):
#     print("All items of list are equals to the string.")

# else:
#     print("All the items of list are not equals to the string.")

'''
56. Write a python program to replace the element in a list with another list.
Sample data : [1, 3, 5, 7, 9, 10], [2, 4, 6, 8]
Expected Output: [1, 3, 5, 7, 9, 2, 4, 6, 8]
'''

# li56 = [1, 3, 5, 7, 9, 10]
# li56_1 = [2, 4, 6, 8]

# li56.pop()
# li56 += li56_1

# print(li56)

'''
57. Write a python program to check whether the n-th element exists in a given list.
'''

# li57 = [1, 3, 5, 7, 9, 2, 4, 6, 8]
# num = 5

# if num in li57:
#     print("Number do exists.")
# else:
#     print("Number does not exists.")

'''
58. Write a python program to find a tuple, the smallest second index from a list of tuples.
'''

# li58_1 = [0, 10, (30, 20), 40, 50, (80, 70, 60), (110, 90, 100, 120)]
# li58_2 = []

# for x in li58_1:
#     if isinstance(x, tuple):
#         for y in x:
#             li58_2.append(y)

# li58_2.sort()
# print("Sorted list of the elements of tuples:", li58_2)
# print("Smallest second index from the list of the elements of tuples contains-", li58_2[1])

'''
59. Write a python program to create a list of empty dictionaries.
'''

# li59 = []
# for x in range(10):
#     li59.append({})

# print(li59)

'''
60. Write a python program to print a list of space-separated elements.
'''

# li60 = [1, 2, 3, 4]

# for x in li60:
#     print(str(x), end=" ")

'''
61. Write a python program to insert a given string at the beginning of all items in a list.
Sample list : [1,2,3,4], string : emp
Expected output : ['emp1', 'emp2', 'emp3', 'emp4']
'''

# li61 = [1, 2, 3, 4]
# li61_1 = []
# string = 'emp'
# x = 0

# while x in range(len(li61)):
    
#     y = string + str(li61[x])
#     li61_1.append(y)

#     x += 1

# print(li61_1)

'''
62. Write a python program to iterate over two lists simultaneously.
'''

# li62 = [1, 2, 3, 4, 5]
# li62_1 = ['a', 'b', 'c', 'd', 'e']
# count62 = 0

# for x in li62:
#     print(x, li62_1[count62])
#     count62 += 1

'''
63. Write a Python program to move all zero digits to end of a given list of numbers. 
Expected output:
Original list:
[3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]
Move all zero digits to end of the said list of numbers:
[3, 4, 6, 2, 6, 7, 6, 9, 10, 7, 4, 4, 5, 3, 2, 9, 7, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
'''

# li63 = [3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]
# li63_1 = []

# for x in li63:
#     if x == 0:
#         li63_1.append(x)
#         li63.remove(x)

# for x in li63:
#     if x == 0:
#         li63_1.append(x)
#         li63.remove(x)

# for x in li63:
#     if x == 0:
#         li63_1.append(x)
#         li63.remove(x)
# print(li63)
# print(li63_1)

# li63_3 = li63 + li63_1
# print(li63_3)

'''
64. Write a python program to find the list in a list of lists whose sum of elements is the highest.
Sample lists: [1,2,3], [4,5,6], [10,11,12], [7,8,9]
Expected Output: [10, 11, 12]
'''



'''
65. Write a python program to find all the values in a list are greater than a specified number.
'''

# li65 = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]

# for x in li65:
#     if x >= 5:
#         print(x, end=" ")

'''
66. Write a Python program to extend a list without append. 
Sample data: [10, 20, 30]
[40, 50, 60]
Expected output : [40, 50, 60, 10, 20, 30]
'''

# li66 = [10, 20, 30]
# li66_1 = [40, 50, 60]

# li66_1 += li66

# print(li66_1)

'''
67. Write a Python program to remove duplicates from a list of lists. 
Sample list : [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
New List : [[10, 20], [30, 56, 25], [33], [40]]
'''

li67 = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
# x = 1
# temp = li67[0]

# while x in range(len(li67)):
    
#     if li67[x] == temp:
#         li67.remove(li67[x])
#         temp = li67[x+1]
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#     temp = li67[x]
#     x += 1

# print(li67)

'''
68. Write a Python program to check whether all dictionaries in a list are empty or not. 
Sample list : [{},{},{}]
Return value : True
Sample list : [{1,2},{},{}]
Return value : False
'''

# li68 = [{},{},{}]
# li68_1 = [{1,2},{},{}]
# count = 0

# for x in li68:
#     if len(x) == 0:
#         count += 1
#     else:
#         break

# if count != 0:
#     print(True)
# else:
#     print(False)

'''
69. Write a Python program to flatten a given nested list structure. 
Original list: [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
Flatten list:
[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
'''

# li69 = [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
# li69_1 = []

# for x in li69:
#     if isinstance(x, list) or isinstance(x, tuple):
#         for y in x:
#             li69_1.append(y)
    
#     else:
#         li69_1.append(x)

# print(li69_1)

'''
70. Write a Python program to remove consecutive duplicates of a given list. 
Original list:
[0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
After removing consecutive duplicates:
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]
'''



'''
71. Write a Python program to pack consecutive duplicates of a given list elements into sublists. 
Original list:
[0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
After packing consecutive duplicates of the said list elements into sublists:
[[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]]
'''



'''
72. Write a Python program to decode a run-length encoded given list. 
Original encoded list:
[[2, 1], 2, 3, [2, 4], 5, 1]
Decode a run-length encoded said list:
[1, 1, 2, 3, 4, 4, 5, 1]
'''

# li72 = [[2, 1], 2, 3, [2, 4], 5, 1]
# li72_1 = []

# for x in li72:
#     if isinstance(x, list) or isinstance(x, tuple):
#         for y in x:
#             li72_1.append(y)
    
#     else:
#         li72_1.append(x)

# print(li72_1)

'''
73. Write a Python program to split a given list into two parts where the length of the first part of the list is given. 
Original list:
[1, 1, 2, 3, 4, 4, 5, 1]
Length of the first part of the list: 3
Splited the said list into two parts:
([1, 1, 2], [3, 4, 4, 5, 1])
'''


'''
74. Write a Python program to remove the K'th element from a given list, print the new list. 
Original list:
[1, 1, 2, 3, 4, 4, 5, 1]
After removing an element at the kth position of the said list:
[1, 1, 3, 4, 4, 5, 1]
'''

# li78 = [1, 1, 2, 3, 4, 4, 5, 1]

# li78.remove(2)
# print(li78)

'''
75. Write a Python program to insert an element at a specified position into a given list. 
Original list:
[1, 1, 2, 3, 4, 4, 5, 1]
After inserting an element at kth position in the said list:
[1, 1, 12, 2, 3, 4, 4, 5, 1]
'''

# li75 = [1, 1, 2, 3, 4, 4, 5, 1]

# li75.insert(2, 12)
# print(li75)

'''
76. Write a python program to extract a given number of randomly selected elements from a given list.
Original list: [1, 1, 2, 3, 4, 4, 5, 1]
Selected 3 random numbers of the list: [4, 4, 1]
'''

# li76 = [1, 1, 2, 3, 4, 4, 5, 1]
# print(random.choices(li76, k = 5))

'''
77. Write a Python program to generate the combinations of n distinct objects taken from the elements of a given list. 
Original list: [1, 2, 3, 4, 5, 6, 7, 8, 9] 
Combinations of 2 distinct objects: [1, 2] [1, 3] [1, 4] [1, 5] .... [7, 8] [7, 9] [8, 9]
'''



'''
78. Write a python program to round every number of a given list of numbers and print the total sum multiplied by the length of the list.
Original list: [22.4, 4.0, -16.22, -9.1, 11.0, -12.22, 14.2, -5.2, 17.5]
Result: 243
'''

# li78 = [22.4, 4.0, -16.22, -9.1, 11.0, -12.22, 14.2, -5.2, 17.5]
# sum = 0

# for x in li78:
#     sum += int(x)

# print(sum * len(li78))

'''
79. Write a python program to round the numbers of a given list, print the minimum numbers and multiply the numbers by 5. 
Print the unique numbers in ascending order separated by space.
Original list: [22.4, 4.0, -16.22, -9.1, 11.0, -12.22, 14.2, -5.2, 17.5]
Minimum value: 4
Maximum value: 220
Result: 20 25 45 55 60 70 80 90 110
'''



'''
80. Write a python program to create a multidimensional list (lists of lists) with zeros.
Multidimensional list: [[0, 0], [0, 0], [0, 0]]
'''

# li80 = []

# for x in range(3):

#     li80_1 = []
#     for y in range(4):

#         li80_1.append(0)
    
#     li80.append(li80_1)

# print(li80)

'''
81. Write a python program to create a 3x3 grid with numbers.
3x3 grid with numbers: [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
'''

# li81 = []

# for x in range(3):

#     li81_1 =[]
#     for y in range(1,4):

#         li81_1.append(y)

#     li81.append(li81_1)

# print(li81)

'''
82. Write a python program to read a matrix from console and print the sum for each column. Accept matrix rows, columns and elements for each column separated with a space (for every row) as input from the user.
input rows: 2
input columns: 2
input number of elements in a row(1, 2, 3):
1 2
3 4
sum for each column:
4 6
'''



'''
83. Write a python program to read a square matrix from console and print the sum of matrix primary diagonal. Accept the size of square matrix and elements for each column separated with a space (for every row) as input from the user.
Input the size of the matrix: 3
2 3 4
4 5 6
3 4 7
Sum of matrix primary diagonal: 14
'''



'''
84. Write a python program to Zip two given lists of lists.
Original lists:
[[1, 3], [5, 7], [9, 11]]
[[2, 4], [6, 8], [10, 12, 14]]
Zipped list:
[[1, 3, 2, 4], [5, 7, 6, 8], [9, 11, 10, 12, 14]]
'''



'''
85. Write a python program to count number of lists .
Original list:
[[1, 3], [5, 7], [9, 11], [13, 15, 17]]
Number of lists in said list of lists:
4
Original list:
[[2, 4], [[6, 8], [4, 5, 8]], [10, 12, 14]]
Number of lists in said list of lists:
3
'''

# li85_1 = [[1, 3], [5, 7], [9, 11], [13, 15, 17]]
# li85_2 = [[2, 4], [[6, 8], [4, 5, 8]], [10, 12, 14]]

# count85_1 = 0
# count85_2 = 0

# for x in li85_1:
#     if isinstance(x, list):
#         count85_1 += 1

# print("Number of lists in said list of lists:", count85_1)

# for x in li85_2:
#     if isinstance(x, list):
#         count85_2 += 1

# print("Number of lists in said list of lists:", count85_2)
