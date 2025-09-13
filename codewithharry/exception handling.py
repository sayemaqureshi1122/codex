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
    
    
n = input("enter a num: ")
try:
    for i in range(1,11):
        print(f"{int(n)} X {i} = {int(n)*i}")
except ValueError :
    print("invalid input")
    