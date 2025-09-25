#For loop

# '''for loop in range'''
# for i in range(0,9): #range function works from '0 to (n-1)'
#     print(i+1)


# #while loop
# ''' Q1] To print number in decreasing order using while loop.'''
# i = 5
# while(i >= 1):
#     print(i)
#     i -= 1
# print("All done buddy")

# '''Q2] emulate do-while loop in python.
#  logic - prints the loop content once atleast then for next time checks condition'''
 
# while True:
#     i = int(input("enter a no. :"))
#     if i == 3:
#         break
#     print(i)
    

# ''' Q3] print multiplication table of 5 '''
# num = int(input("enter a number:"))
# for i in range(1,11):
#     print(f"{num} X {i} = ", num*i)


# ''' Q4] sum of n natural numbers
# Natural number = starts from 1 to infinte'''
# n = int(input("Enter a number:"))
# count = 0
# while n > 0:
#     count += n
#     n = n-1
# print(count)

# ''' Q5] print right angle triangle'''
# n =int(input("enter a no.:")) 
# for i in range(1,n+1):
#     for j in range(i):
#         print("*", end =" ")
#     print()   


# #do while loop in python
# while True:
#     print("start the game")
#     game = input("Did you win the game....tell (yes/no)")
#     if game == "yes":
#         print("Finally u won >_<")
#         break
    


# ### pattern questions : 
n = 10
for i in range(n):
    count = n-i
    print(' '*i)
    print("*"*(i+1))