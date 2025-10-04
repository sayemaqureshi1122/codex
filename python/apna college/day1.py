# first_name = "tony"
# last_name = "stark"
# age = 51
# is_genius = True
# print(first_name, last_name, is_genius)

# super_hero = input("what is your superhero name? ")
# print("Hello " + super_hero)

# first = int(input("enter a num: "))
# second = int(input("enter a num: "))
# print("result is : " + str(first + second))
# print(super_hero.find('T'))

# #building a calculator
# num1 = int(input("enter num1: "))
# num2 = int(input("enter num2: "))
# operation = input("enter operation u want to perform: (ie. +, -, *, /, //, **, %): ")
# def cal(num1, num2, operation):
#     if operation == "+":
#         print(num1 + num2)
#     elif operation == "-":
#         print(num1 -  num2)
#     elif operation == "/":
#         if num2 > 0:
#             print(num1 / num2)
#         else:
#             print("division with 0 is invalid")
#     elif operation == "*":
#         print(num1 * num2)
#     elif operation == "//":
#         if num2 > 0:
#             print(num1 // num2)
#         else:
#             print("division with zero is invalid")
#     elif operation == "**":
#         print(num1 ** num2)
#     elif operation == "%":
#         print(num1 % num2)
#     else:
#         print("invalid operation")
# cal(num1, num2, operation)

#patterns using for loop

# i = 1
# num = int(input())
# while i <= num:
#     print(i * "*")
#     i += 1

## or
num1 = int(input())   
for i in range(1,num1+1):
    print("*" * i)
      
# num2 = int(input())
for i in range(num1,0,-1):
    print("*" * i)

set1 = set()
print(type(set1))
    