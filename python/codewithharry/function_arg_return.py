''' Q1] Create a function add_two_numbers(a, b) that returns the sum of two numbers.'''
def add_two_numbers(a,b):
    return a+b
c = add_two_numbers(5,6)
print(c)

''' Q2] Write a function get_greeting() that returns "Good morning!", and store it in a variable called message. Print the message.'''
def get_greeting():
    return "GOOD MORNING!"
b = get_greeting()
print(b)

''' Q3] Define a function get_alarm_time() that returns "6:30 AM". Use this returned value to decide what you’ll do (e.g., "Time to wake up").'''
def get_alarm_time():
    return "6:30 AM"
c = get_alarm_time()
if c == "6:30 AM":
    print("time to wake up buddy!!")
else:
    print("You can sleep more sleepyhead")
    
''' Q4] Imagine a function get_weather_report() that returns "Rainy". Based on the return value, decide whether to carry an umbrella.'''
def get_weather_report():
    return "rainy"
n = get_weather_report()
if n == "sunny":
    print("use an sunscreen bitch")
elif n == "rainy":
    print("remember to carry an umbrella girl!!")
else:
    print("Just go out and SLAY!!!!")
    
''' Q5] Create a function square(n) that returns the square of a number. Then use that return value in another function to add 10 to it.'''
def square(n):
    return n * n

b = square(4)
print(b)

def add():
    return b + 10

v = add()
print(v)

''' Q6] Create a function is_even(n) that returns True if the number is even, else returns False. Use return, don’t print.'''
def is_even(n):
    if n % 2 == 0:
        return True
    else: 
        return False
n = is_even(10)
print(n)

''' Q7] Write a function that returns the length of a string without using len(). (Try using a loop and return)'''
def str_len(b):
    count = 0
    for i in b:
        count += 1
    return count

f = str_len("anil")
print(f)

''' Q8]Write a function get_items_in_bag() that returns a list of 3 strings like ["Pen", "Notebook", "Charger"]. Then print the number of items using a built-in function.'''
def get_items_in_bag(*names):
    for i in names:
        return len(names)
    
h = get_items_in_bag("pen", "Notebook", "charger")
print(h)
     
#Q9] Avg of three numbers
def avg_num(a, b, c):
    avg = (a + b + c) / 3
    return avg
d = avg_num(4, 2, 7)
print(d)

# Q10] to print the len of parameter list
def to_print_len(s):
    print(len(s))
    
to_print_len("sayema")

# Q11] to print element of list indivisually
def print_ele(s):
    for i in s:
        print(i)
print_ele("sayema")

# Q12] find factorial of n
def factorial(n):
    return n * (n - 1)

c = factorial(7)
print(c)

# Q13] convert usd to inr
def convert_money(n):
     return n * 87.58
m = convert_money(2)
print(m)

x = "good"
def hello():
    global x
    x *= 2
    print("hello", x)
hello()



    