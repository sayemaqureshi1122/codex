# T = int(input("enter a num: "))
# while (T):
#     try:
#         a, b = map(int, input().split())
#         print(a/b)
#     except ZeroDivisionError as e:
#         print("Error Code:", e)
#     except ValueError as v:
#         print("Error Code:", v)
#     T -= 1
    
    
# n = input("enter a num: ")
# try:
#     for i in range(1,11):
#         print(f"{int(n)} X {i} = {int(n)*i}")
# except ValueError :
#     print("invalid input")


# #FINALLY CLAUSE
# def fun1():
#     list = [1, 2, 3, 4]
#     try:
#         i = int(input("enter a index: "))
#         return(list[i])    
#     except:
#         return("error occurs")
#     finally:
#         print("i am always executed")
# x = fun1()
# print(x)

#CUSTOM ERROR
a = input("enter a value between 5 and 9: ")
try:
    if a < 5 or a > 9:
            raise ValueError("the value is not between 5 and 9")
finally :
    if a == "quit":
        print(a)
    



