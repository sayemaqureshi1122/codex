
# # to comment multiple line (cmd+/) or ''' ...''' or """ ...."""

# ## All about print statement

# #Escape sequence characters
# print("hello world! \n this is my first program") #\n - new line
# print("hello world , this is my \"first\" program") # \"...\" || ('..."highlight text"..') -- to highlight the code
# print("hello","sayema","goodmorning", sep="-" , end=" 11") #using sep and end para
# print( "todays date is:",29,6,2025 ,sep="-")

# #data types
# a = 1 
# b = 3.14
# c = "sam"
# d = True
# e = complex(2,3)
# list = [1,2,3,["hello"],[5,6],["@@@"]] #only diff betn list and tuple is list are muttable and tuples are not.
# tuple = (("apple","mango"),(1,2,3),("a,b"))
# dict = {"name": "sam", "age": 21, "address":"ngp"}
# print(a,b,c,d,e,list,tuple,dict)
# print(type(a), type(b),type(c),type(d), type(e), type(list),type(tuple), type(dict))

# #operators
# print(2+3) 
# print(2-3)
# print(2*3)
# print(2/3)
# print(2%3)
# print(2//3) #floor division only give int part of division leaving the decimal part
# print(2**3) #exponential

# question 1: create a calc capable of performing add, sub, mul, div on two num ur program should format trh output in readable manner
# def calc(a,b):
#     operation=input("enter add/sub/mul/div to perform operation:")
#     if operation == "add":
#         return a+b
#     if operation == "sub":
#         return a-b
#     if operation == "mul":
#         return a*b
#     if operation == "div":
#         return a/b
# res=calc(5,4)
# print(res) 
# #or
# a=3
# b=4
# print('add is:',a+b)
# print('sub is:',a-b)
# print('mul is:',a*b)
# print('div is:',a/b)

# #type casting
# a = 3
# b = 4.4
# print(type(a), type(b))
# print(a + b) #implicit
# c = "9"
# print(type(a), type(c))
# print(int(c) + b) #explicit 

# #user input
# a = input("digit: ")
# b = input("2nd digit: ")
# print(a+b) #takes default datatype as string only works for "+" operator
# print(int(a)/int(b)) #so explicitly define datatype

#Match cases
sam = int(input("enter a integer value:"))
match sam:
    case _ if sam < 0 :
        print("hello sir that's not an integer")
    case _ if sam >= 0 and sam < 40 :
        print(sam ," is in range less than 40")
    case _ if sam == 80 :
        print("number is 80")
    case _ :
        print("f{sam} does not match any cases")


for num in range (11,1,-3):
    print(num)

name = "sayema"
for i in name:
    print(i , end =" ,")

arr =["red" ,"green" ,"blue" ,"pink"]
for col in arr:
    print(col)
    for alph in col:
        print(alph)




