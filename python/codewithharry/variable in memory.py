## How a variable is stored in the memory??
'''
ans -- look in traditional languages like c, java does not change the address when the value of var changes it 
just updates its value, hence having the same address.
But in python we already have  commonly used nums, string stored in different address so when we change the values of a var
it just points to that address.


Ex:
House analogy explained below...
'''
#For c, java
Age = 20  #→ House #1001 is built with a nameplate “Age”, and inside it is 20.
Age = 30  #The same house #1001 still has the nameplate “Age”, but the old furniture 20 is removed and replaced with 30.
print(id(Age)) # it will print same id for both age for c and java.

#For python 
a = 10     #A house with 10 already exists. Python takes a sticky note “Age” and sticks it on that house.      
print(id(a))    

a = 20   #Python does not repaint the old house. Instead, it removes the sticky note “Age” from the house of 10, and sticks it on the house of 20.       

print(id(a))    

#prints different values for both the a's.


 