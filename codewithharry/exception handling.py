T = int(input("enter a num: "))
while (T):
    try:
        a, b = map(int, input().split())
        print(a/b)
    except ZeroDivisionError as e:
        print("Error Code:", e)
    except ValueError as v:
        print("Error Code:", v)
    T -= 1
    
    