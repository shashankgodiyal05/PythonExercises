# 1. Write a python script to sort (ascending and descending) a dictionary by value.


dictionary1 = {1 : 10, 3 : 30, 5 : 50, 2 : 20, 4 : 40, 6 : 60}
dictionary1_1 = {}
li1 = []

li1 = list(dictionary1.values())

li1.sort()

for x in li1:
    y = dictionary1.get(x)
    dictionary1_1.setdefault(x, y)

print(dictionary1_1)



# 2. Write a python scripe to add a key to a dictionary.
# Sample Dictionary: {0 : 10, 1 : 20}
# Expected Result: {0 : 10, 1 : 20, 2 : 30}


dictionary2 = {0 : 10, 1 : 20}

dictionary2[2] = 30
print(dictionary2)



# 3. Write a python script to concatenate following dictionaries to create a new one.
# Sample Dictionary: dic1 = {1 : 10, 2 : 20}
# dic2 = {3 : 30, 4 : 40}
# dic3 = {5 : 50, 6 : 60}
# Expected result: {1 : 10, 2 : 20, 3 : 30, 4 : 40, 5 : 50, 6 : 60}


dictionary3_1 = {1 : 10, 2 : 20}
dictionary3_2 = {3 : 30, 4 : 40}
dictionary3_3 = {5 : 50, 6 : 60}

items_ = []

items3_1 = []
items3_1 = dictionary3_1.items()

items3_2 = []
items3_2 = dictionary3_2.items()

items3_3 = []
items3_3 = dictionary3_3.items()

for x in items3_1:
    items_.append(x)

for x in items3_2:
    items_.append(x)

for x in items3_3:
    items_.append(x)

print(dict(items_))



# 4. Write a python script to check whether a given key already exists in a dictionary.


dictionary4 = {1 : 10, 2 : 20, 3 : 30, 4 : 40, 5 : 50, 6 : 60}
li4 = []
num = 4
count = 0
li4 = dictionary4.keys()

for x in li4:
    if num == 4:
       count = 1

if count == 0:
    print("Given key does not exists in a dictionary.")
else:
    print("Given key already exists in a dictionary.")



# 5. Write a python program to iterate over dictionaries using for loops.


dictionary5 = {1 : 10, 2 : 20, 3 : 30, 4 : 40, 5 : 50, 6 : 60}

for x in dictionary5.items():
    print(x)



# 6. Write a python script to generate and print a dictionary that contains a number between 1 and n in the form (x, x*x).
# Sample Input: n = 5
# Expected Output: {1 : 1, 2 : 4, 3 : 9, 4 : 16, 5 : 25}


dictionary6 = {}
x =1

n = int(input("Enter a number: "))

while x in range(n + 1):
    
    dictionary6.setdefault(x, x*x)
    x += 1

print(dictionary6)



# 7. Write a python script to print a dictionary where the keys are numbers between 1 and 15 both included and the values are square of keys.
# Expected output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}


dictionary6 = {}
x = 1

while x in range(16):
    
    dictionary6.setdefault(x, x*x)
    x += 1

print(dictionary6)



# 8. Write a python script to merge two python dictionaries.


dictionary8_1 = {1 : 10, 2 : 20, 3 : 30, 4 : 40, 5 : 50, 6 : 60}
dictionary8_2 = {7 : 70, 8 : 80, 9 : 90}

dictionary8_1.update(dictionary8_2)

print(dictionary8_1)


# 9. Write a python program to iterate over dictionaries using for loops.


dictionary9 = {1 : 10, 2 : 20, 3 : 30, 4 : 40, 5 : 50, 6 : 60}

for x in dictionary9.items():
    print(x)



# 10. Write a python program to sum all the items in a dictionary.


dictionary10 = {1 : 10, 2 : 20, 3 : 30, 4 : 40, 5 : 50, 6 : 60}

li10_1 = []
li10_1 = dictionary10.keys()

li10_2 = []
li10_2 = dictionary10.values()

print("Sum of the keys of the dictionary:", sum(li10_1))
print("Sum of the values of the dictionary:", sum(li10_2))



# 11. Write a python program to multiply all the items in a dictionary.


dictionary11 = {1 : 10, 2 : 20, 3 : 30, 4 : 40, 5 : 50, 6 : 60}
result_keys = 1
result_values = 1

li11_1 = []
li11_1 = dictionary11.keys()

li11_2 = []
li11_2 = dictionary11.values()

for x in li11_1:
    result_keys *= x

for x in li11_2:
    result_values *= x

print("Result after multiplying all the keys of the dictionary:", result_keys)
print("Result after multiplying all the values of the dictionary:", result_values)



# 12. Write a python program to remove a key from a dictionary.


dictionary12 = {1 : 10, 3 : 30, 5 : 50, 2 : 20, 4 : 40, 6 : 60}

dictionary12.pop(5)
print(dictionary12)



# 13. Write a python program to map two lists into a dictionary.


li13_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
li13_2 = [10, 20, 30, 40, 50, 60, 70, 80, 90]
count = 0

dictionary13 = {}

dictionary13 = dictionary13.fromkeys(li13_1)

for x in dictionary13:
    dictionary13[x] = li13_2[count]
    count += 1

print(dictionary13)



# 14. Write a python program to sort a dictionary by key.


dictionary1 = {1 : 10, 3 : 30, 5 : 50, 2 : 20, 4 : 40, 6 : 60}
dictionary1_1 = {}
li1 = []

li1 = list(dictionary1.keys())

li1.sort(reverse=True)

for x in li1:
    y = dictionary1.get(x)
    dictionary1_1.setdefault(x, y)

print(dictionary1_1)



# 15. Write a python program to get maximum and minimum value in a dictionary.


dictionary15 = {1 : 10, 3 : 30, 5 : 50, 2 : 20, 4 : 40, 6 : 60}
li15 = []

li15 = dictionary15.values()

print(max(li15))
print(min(li15))


