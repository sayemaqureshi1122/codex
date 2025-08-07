#Write a code for fibonacci series?

''''logic f(n) = f(n-1) + f(n-2)'''
def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(3))
print(fibonacci(6))

#to print the sequence
a = int(input("enter a int: "))
for i in range(a):
    print(fibonacci(i))
    
# Q2] try making a empty set and check its type
set1 = set()
print(type(set1))

#Q3] factorial using recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return  n * factorial(n - 1)
print(factorial(5))

#Q4] print Countdown
def countdown(n):
    if n == 0 or n == 1:
        return n
    else:
        print(n)
        return countdown(n - 1)

print(countdown(7))

# Q5] sum of natural numbers
def natural(n):
    if n == 0 or n == 1:
        return n
    else:
        return n + natural(n - 1)
    
print(natural(4))


print("hello", "world")
print(1,2,3,4,5)

for i in range(1,6):
    print( f"{i} - {i * i}")
    
ip =input().strip().split()
print(ip)
com = "sam"
web = "q"
print(input())


            
