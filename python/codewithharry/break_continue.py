# break - loop se bahar 
# continue - iteration se bahar
''' Q1] Print numbers from 1 to 10. Stop printing if the number is 5.'''
#USING WHILE LOOP
num = int(input("Enter any number:"))
while(num < 10):
    if num == 5:
        break
    print(num)
    num = num + 1
#USING FOR LOOP
for num in range(1,10):
    if num == 5:
        break
    print(num)
    
''' Q2] Take user input continuously. Break the loop if user types "exit".'''
ip = ""
while( ip != "exit"):
    ip  = input("enter entry or exit:")
    if ip == "exit":
        break
    print(ip)

''' Q3] Find the first three number divisible by 7 between 1 and 100.'''
for num in range (1,100):
    if num % 7 == 0:
        if num > 21:
            break
        print(num)

''' Q4] Keep asking for a number from user. Stop asking when they enter a negative number.'''
while(num):
    num = int(input("number:"))
    if num <= 0:
        break
    print(num)

''' Q5] Loop from 1 to 100, break the loop when you find the first perfect square.'''
for i in range(1,100):
    for j in range(i):
        num = j * j
        if num == i:
            print(num)
            break
    if j * j == i:
        break
    
#USING CONTINUE
''' Q6] Print numbers from 1 to 10, but skip printing 5.'''
for i in range(1,10):
    if i == 5:
        continue
    print(i)

''' Q7] Loop through numbers 1 to 20, print only odd numbers (use continue).'''
for i in range(1,20):
    if i % 2 == 0:
        continue
    print(i)

''' Q9] Print numbers from 1 to 10, but skip all multiples of 3.'''
for i in range(1,10):
    if i % 3 == 0:
        continue
    print(i)

''' Q10 Loop through characters in a string and print only vowels (use continue to skip consonants).'''
name = input('enter any string:')
for i in name:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        print(i, end = ",")
    else:
        continue
print("\nDone")

