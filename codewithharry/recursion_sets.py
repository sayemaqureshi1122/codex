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

#Q11]Write code to assign the number of characters in the string rv to a variable num_chars.

rv = """Once upon a midnight dreary, while I pondered, weak and weary,
    Over many a quaint and curious volume of forgotten lore,
    While I nodded, nearly napping, suddenly there came a tapping,
    As of some one gently rapping, rapping at my chamber door.
    'Tis some visitor, I muttered, tapping at my chamber door;
    Only this and nothing more."""

# Write your code here!
num_chars = len(rv)
print(num_chars)

'''Q12] rainfall_mi is a string that contains the average number of inches of rainfall in Michigan for every month (in inches) 
with every month separated by a comma. Write code to compute the number of months that have more than 3 inches of rainfall. 
Store the result in the variable num_rainy_months. In other words, count the number of items with values > 3.0.'''

rainfall_mi = "1.65, 1.46, 2.05, 3.03, 3.35, 3.46, 2.83, 3.23, 3.5, 2.52, 2.8, 1.85"
rainfall_list = rainfall_mi.split(",")
num_rainy_months = 0
for rain in rainfall_list:
    if float(rain) > 3.0:
        num_rainy_months += 1
print(num_rainy_months)

''' Q14] Write code that counts the number of words in sentence that contain either an “a” or an “e”. Store the result in the variable num_a_or_e.

Note 1: be sure to not double-count words that contain both an a and an e.

HINT 1: Use the in operator.

HINT 2: You can either use or or elif.

Hard-coded answers will receive no credit.'''

sentence = "python is a high level general purpose programming language that can be applied to many different classes of problems."
num_a_or_e = 0
for word in sentence.split():
    if "a" in word or "e" in word:
        num_a_or_e += 1
print(num_a_or_e)



    
