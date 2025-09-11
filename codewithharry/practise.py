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



# n = int(input())
# for i in range(n+1):
#     for j in range(i):
#         print("*", end =" ")
#     print()
    
# N = int(input())
# sum =0
# for i in range(1,N+1):
#     sum += 3*i
# print(sum)

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

# a = 15
# if a > 10:
#     print("u")
# if a > 5:
#     print("v")
    
    
# a, b, c = map(int, input().split())
# if a < b and b < c and a < c :
#     print("increasing")
# elif a > b and b > c and a > c:
#     print("decreasing")
# else:
#     print("neither")
    
# my_tuple = (1,2,3)
# print(my_tuple)

# student_grades = {"Alice": 85, "Bob": 72, "Charlie": 90, "David": 65, "Eva": 88, "John": 45}

# # Complete the code 
# name = input()
# if name in student_grades:
#     print(student_grades[name])
# else:
#     print("Not Found")
# data = [1, 2, 3, 4, 4, 5]
# print(data[0] + data[3])

# n = list(map(int, input().split()))
# print(n[0]*n[2])
# m = 1
# while m > 1:
#     print("h")
    
# n = int(input())
# def fact(n):
#     if n == 0 or n == 1:
#         return n
#     else:
#         return n * fact(n - 1)
# c = fact(n)
# print(c)

# n = int(input().strip())
# sum = 0
# # Update the code below this line
# for i in range(1,n+1):
#     sum += i
# print(sum)

# for i in range(5):
#     if i == 2:
#         continue
#     print(i, end =" ")
    
# values = list(map(int, input().split()))
# # Update your code below this line
# for i in values:
#     if i <= 10:
#         print(i*i)
#     else:
#         continue
    
# def is_even(num):
#     # Complete the function 
#     if num % 2 == 0:
#         return "even"
#     else:
#         return "odd"

# def main():
#     # Complete the function 
#     t = int(input())
#     for i in range(t):
#         num = int(input())
#         c = is_even(num)
#         print(c)
# if __name__ == "__main__":
#     main()

x = int(input("num: "))   
i = 1
while(i < x):
    power = i ** 2
    if power < x:
        print(power, end = " ")
    i += 1
