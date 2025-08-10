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

# Q6] to reverse a string    
def reverse_string(s):
    if len(s) == 0:
        return ""
    return reverse_string(s[1: ]) + s [0]
    
print(reverse_string("magic"))

# Q7] Print numbers from 1 to n using recursion.
def print_asc(n):
    if n == 0:
        return 0
    print(n)
    return  
print(print_asc(5))

#Q8] 
list11 = [1, 2, 3, 1]
for i in list11:
    if i  == i:
        list11.remove(i)
print(list11)
# Q9] sum of n natural numbers       
def sum_of_natural(n):
    if n == 0:
        return 0
    print(n, end = " ") 
    return sum_of_natural(n - 1) + n

sum = sum_of_natural(3)
print()
print(sum)

# Q10] write a recursive function to print all the elements in the list
list1122 = ["thor", "ironman", "spiderman", "caption america", "black widow"]
def ele(list, i):
    if i == len(list):
        return "Done with the execution"
    print(list[i])
    return ele(list , i + 1)
o = ele(list1122, 0)
print(o)

    
