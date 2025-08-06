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