'''
1. Write a python function to find the max of three numbers.
'''
'''
def func(a, b, c):

    if a > b and a > c:
        print("A is greatest")

    elif b > a and b > c:
        print("B is greatest")
        
    else:
        print("C is greatest")

func(23, 4, 6)

'''

'''
2. Write a python function to sum all the numbers in a list.
Sample List: (8, 2, 3, 0, 7)
Expected Output: 20
'''

'''
def list_sum(*param2):

    sum2 = 0
    for x in param2:
        sum2 += x

    print(sum2)

list_sum(8, 2, 3, 0, 7)

'''

'''
3. Write a python function to multiply all the numbers in a list.
Sample List: (8, 2, 3, -1, 7)
Expected Output: -336
'''

'''
def list_multiply(*param3):

    result = 1
    for x in param3:
        result *= x

    print(result)

list_multiply(8, 2, 3, -1, 7)

'''

'''
4. Write a python program to reverse a string.
Sample String: "1234abcd"
Expected Output: "dcba4321"
'''

'''
def reverse_string(s):

    print(s[-1 : : -1])

reverse_string("1234abcd")

'''

'''
5. Write a python function to calculate the factorial of a number (a non-negetive integer). the function accepts the number as an argument.
'''

'''
def factorial(n):

    f = 1
    for x in range(n, 0, -1):
        f *= x
    
    return f

print(factorial(6))

'''

'''
6. Write a python function to check whether a number is in a given range.
'''

'''
def check_in_range(num6):

    if num6 in range(20):
        print("Entered number comes in the range.")
    
    else:
        print("Entered number does not comes in the range.")

check_in_range(5)
check_in_range(23)

'''

'''
7. Write a python function that accepts a string and calculate the number of upper letters and lower case letters.
Sample String: "The quick Brown Fox"
Expected Output:
No. of Upper case characters: 3
No. of Lower case characters: 12
'''
'''
def count_u_l(s):

    l = 0
    u = 0

    for x in s:
        if x.islower():
            l += 1

        elif x.isupper():
            u += 1

    print("upper cases :", u)
    print("lower cases :", l)

count_u_l("Mera naam Shinchan hai me shararat se bhara, badi mushkil me padi meri family Nohara")

'''

'''
8. Write a python function that takes a list and returns a new list with unique elements of the first list.
Sample List: [1, 2, 3, 3, 3, 3, 4, 5]
Unique List: [1, 2, 3, 4, 5]
'''

'''
def unique_list(*param8):
    li8_1 = []

    for x8 in param8:
        li8_1.append(x8)

    st = set(li8_1)
    li8_1 = list(st)

    return li8_1

li8_2 =[]

li8_2 = unique_list(1, 2, 3, 3, 3, 3, 4, 5)
print(li8_2)

'''

'''
9. Write a python function that takes a number as a parameter and check the number is prime or not.
Note: A prime is a natural number greater than 1 and that has no positive divisors other than 1 and itself.
'''

'''
def check_prime(num):
  
    for x in range(2, num):
        if num %x == 0:
            return False

    else:
        return True

print(check_prime(5))

'''

'''
10. Write a python program to print the even numbers from a given list.
Sample List: [1, 2, 3, 4, 5, 6, 7, 8, 9]
Expected Result: [2, 4, 6, 8]
'''

'''
def even_list(*param10):
    
    li10_1 = []
    for x10 in param10:
        
        if x10 % 2 == 0:
            li10_1.append(x10)
    
    return li10_1

li10_2 = []
li10_2 = even_list(1, 2, 3, 4, 5, 6, 7, 8, 9)

print(li10_2)

'''