

"""
1- Write a Python program which accepts the user's first and last name and print them in
reverse order with a space between them.
"""
# first_name = input("Enter your first name: ")
# last_name = input("Enter your last name: ")
# print(last_name + " " + first_name)

#*****************************************************************************************

"""
2- Write a Python program that accepts an integer (n) and computes the value of
n+nn+nnn.
Sample value of n is 5
Expected Result : 615
"""
# n = int(input("Enter an integer value for n: "))
# result = n + int(str(n) + str(n)) + int(str(n) + str(n) + str(n))
# print("Result:", result)

#*****************************************************************************************

"""
3- Write a Python program to print the following here document.
Sample string :
a string that you "don't" have to escape
This
is a ....... multi-line
heredoc string --------> example
"""
# print('''a string that you "don't" have to escape
# This
# is a ....... multi-line
# heredoc string --------> example''')

#******************************************************************************************

"""
4- Write a Python program to get the volume of a sphere with radius 6.
"""
# import math
# radius = 6
# volume = (4/3) * math.pi * (radius ** 3)
# print("Volume of the sphere with radius 6:", volume)

#******************************************************************************************

"""
5- Write a Python program that will accept the base and height of a triangle and compute
the area.
"""
# base = float(input("Enter the base of the triangle: "))
# height = float(input("Enter the height of the triangle: "))
# area = 0.5 * base * height
# print("Area of the triangle:", area)

#******************************************************************************************

"""
6- Write a Python program to construct the following pattern, using a nested for loop.
Search about method
end=””
*
**
***
****
*****
****
***
**
*
"""
# max_rows = 5
# for i in range(max_rows):
#     print("*" * (i + 1))
#
# for i in range(max_rows - 1, 0, -1):
#     print("*" * i)

#*******************************************************************************************

"""
7- Write a Python program that accepts a word from the user and reverse it.
"""
# word = input("Enter a word: ")
# reversed_word = word[::-1]
# print("Reversed word:", reversed_word)

#*******************************************************************************************

"""
8- Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
"""
# for num in range(7):
#     if num != 3 and num != 6:
#         print(num)

#********************************************************************************************

"""
9-Write a Python program to get the Fibonacci series between 0 to 50
Note : The Fibonacci Sequence is the series of numbers :
0, 1, 1, 2, 3, 5, 8, 13, 21, ....
Every next number is found by adding up the two numbers before it.
Expected Output : 1 1 2 3 5 8 13 21 34
"""
# fib1, fib2 = 0, 1
# print(fib2, end=" ")
#
# while fib2 < 50:
#     fib1, fib2 = fib2, fib1 + fib2
#     if fib2 < 50:
#         print(fib2, end=" ")

#*********************************************************************************************

"""
10- Write a Python program that accepts a string and calculate the number of digits and
letters.
"""
# input_string = input("Enter a string: ")
#
# num_digits = 0
# num_letters = 0
#
# for char in input_string:
#     if char.isdigit():
#         num_digits += 1
#     elif char.isalpha():
#         num_letters += 1
#
# print("Number of digits:", num_digits)
# print("Number of letters:", num_letters)

#***********************************************************************************************


