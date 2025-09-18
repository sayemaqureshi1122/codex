# #1]
# print("Welcome to the Coding Village! 🥷")

# #2]
# name = input("What is your name, adventurer?: ")

# #3]
# print(f"Greetings, {name} Your journey begins now.")

# #4] inout and print
# print("Welcome, adventurer!")
# favcolor = input("what is your fav color adventurer: ")
# print(f"Ah, so your favorite color is {favcolor}. Interesting choice!")
# age = int(input("what is your age: "))
# if age >= 18:
#     print("You are an adult adventurer!")
# else:
#     print("You are still training, young adventurer!")
# #5] arthemetic operations
# # a, b = map(int, input("enter numbers: ").split())
# a = int(input("Enter 1st num: "))
# b = int(input("Enter 2nd num : "))
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a % b)

# #6] loops
# n = int(input("enter a num: "))
# for i in range(1, n + 1):
#     print(i)

# #7] Function
# def welcome():
#     print("Welcome, brave adventurer!")
#     print("Your journey continues...")
# welcome()
# #8]
# def attack(enemy, weapon):
#     if weapon == "sword":
#         return(f"You slashed the {enemy}! with a {weapon}")
#     elif weapon == "bow":
#         return(f"You shot an arrow at the {enemy}")
#     elif weapon == "axe":
#         return f"You smashed the {enemy} with an {weapon}"
#     elif weapon == "magic":
#         return f"You cast a powerful spell on the {enemy}!"
#     else:
#         return(f"You attacked the {enemy} with a {weapon}!")
# msg = attack("dragon", 'sword')
# print(msg)
# msg1 = attack("tree", "axe")
# print(msg1)
# msg2 =  attack("bird", "bow")
# print(msg2)

# print("I\nlove\nCodeChef")
# print("i", "love", "codechef",sep = "\n")


# #9]
# n = int(input())
# for i in range(n+1):
#     for j in range(i):
#         print("*", end =" ")
#     print()

# #10]    
# N = int(input())
# sum =0
# for i in range(1,N+1):
#     sum += 3*i
# print(sum)
# #11]
# num = int(input())
# # Update your code below this line
# while(num > 0):
#     i = 1
#     print(i*i)
#     i += 1
#     num -= 1
# for i in range (1,6):
#     print(i*i)
# s = "Coding on CodeChef"
# print(f"Coding - {len("coding")}")
# print(f"on - {len("on")}")
# print(f"CodeChef - {len("CodeChef")}")
# print(f"{s} - {len(s)}")

# #12]
# a = 15
# if a > 10:
#     print("u")
# if a > 5:
#     print("v")
    
# #13]   
# a, b, c = map(int, input().split())
# if a < b and b < c and a < c :
#     print("increasing")
# elif a > b and b > c and a > c:
#     print("decreasing")
# else:
#     print("neither")

# #14]   
# my_tuple = (1,2,3)
# print(my_tuple)

# #15]
# student_grades = {"Alice": 85, "Bob": 72, "Charlie": 90, "David": 65, "Eva": 88, "John": 45}

# #16]
# # Complete the code 
# name = input()
# if name in student_grades:
#     print(student_grades[name])
# else:
#     print("Not Found")
# data = [1, 2, 3, 4, 4, 5]
# print(data[0] + data[3])

# #17]
# n = list(map(int, input().split()))
# print(n[0]*n[2])
# m = 1
# while m > 1:
#     print("h")

# #18]    
# n = int(input())
# def fact(n):
#     if n == 0 or n == 1:
#         return n
#     else:
#         return n * fact(n - 1)
# c = fact(n)
# print(c)

# #19]
# n = int(input().strip())
# sum = 0
# # Update the code below this line
# for i in range(1,n+1):
#     sum += i
# print(sum)

# #19]
# for i in range(5):
#     if i == 2:
#         continue
#     print(i, end =" ")

# #20]    
# values = list(map(int, input().split()))
# # Update your code below this line
# for i in values:
#     if i <= 10:
#         print(i*i)
#     else:
#         continue

# #21]   
# def is_even(num):
#     # Complete the function 
#     if num % 2 == 0:
#         return "even"
#     else:
#         return "odd"

# #22]
# def main():
#     # Complete the function 
#     t = int(input())
#     for i in range(t):
#         num = int(input())
#         c = is_even(num)
#         print(c)
# if __name__ == "__main__":
#     main()

# 23]
# x = int(input("num: "))   
# i = 1
# while(i < x):
#     power = i ** 2
#     if power < x:
#         print(power, end = " ")
#     i += 1
# print()
# N = int(input("num: "))   
# for i in range(1,11):
#     print(N*i, end = " ")

# #24]
# set1 = {"hello", 1, 2}
# set1.add(9)
# print(set1)
# set1.remove("hello")
# print(set1)
# a = sum(set1)
# print(a)

# #25]
# a = ""
# while(a):
#     print("hello")
    
# #26]
# name = input()
# age = int(input())
# print("The name of the person is",name, "and the age is",age)
# print("The name of the person is", name, "and the age is", age + ".")

# #27] 
 #Your code goes here

# ch = input().strip()   # take input (strip removes extra spaces)

# if 'A' <= ch <= 'Z':      # check uppercase
#     print(1)
# elif 'a' <= ch <= 'z':    # check lowercase
#     print(0)
# else:                     # not an alphabet
#     print(-1)
    
# #28] question on if-else
   
# from os import *
# from sys import *
# from collections import *
# from math import *

# #Your code goes here

# basic = int(input())
# grade = input()
# if grade.isupper():
#     print("Good")
# else:
#     print("grade should be in uppercase")
    
# if grade == "A":
#     allow = 1700
# elif grade == "B":
#     allow = 1500
# else:
#     allow = 1300

# hra = (20/100)*basic
# da = (50/100)*basic
# pf = (11/100)*basic

# total_salary = (basic+hra+da+allow)-pf
# print(round(total_salary))    

# #29]

# word = input("enter a word: ").split()
# print(word)
# list1 = list(word)
# print(list1[0][0])
# operation = input("enter do you want to encrypt or decrypt the code: ")


# #30]
# N = int(input())
# sum = 0
# for i in range(1, N+1):
#     if i % 2 == 0:
#         sum += i
# print(sum)

# #31] 
from os import *
from sys import *
from collections import *
from math import *

#Your code goes here
S = int(input())
E = int(input())
W = int(input())
for i in range(S, E, W):
    celsius = (i - 32)* (5/9)
    print(f"{i} - {int(celsius)}")




# for i in list1:
#     if operation == "encrypt" or "Encrypt" or "ENCRYPT":
#         if len(i) > 3:
#             list1[i].reverse()
#         else:
#             list1[0] = list1[1:len(list1[0])]
#             print(list1)