marks=int(input("enter marks:"))
if marks >=60:
    if marks>=70:
        if marks>=80:
            if marks>=90:
                print("A")
            else:
                print("B")
        else:
            print("C")
    else:
        print("D")
else:
    print("fail")

# a=1
# b=2
# c=3
# if a > b and a>c:
#     print(a)
# if b > a and b > c:
#     print(b)
# if c > a and c > a:
#     print(c)
    
# year=2000
# if (year%4 ==0 and year%100 !=0) or (year%400==0):
#     print(year, " is a leap year")
# else:
#     print( year,"not a leap year")

# #reverse a int
# n = int(input("enter a number: "))
# res = 0
# while n >= 0:
#     d = n % 10
#     res = res * 10 + d
#     n = n // 10
# print(res)
 

# # Q1] to print GM,GA,GE greetings

# #note - in this code make sure to change dt of time as in string it goes serially ex: if "10:00" and "12:00"
# # it will give 10 greater s 0 comes first so it is advisable to convert iy=t into int to get better results
# import time
# ct=int(time.strftime("%H:%M"))
# print(ct)
# if ct>"00:00" and ct < "12:00":
#     print("GM")
# elif ct > "12:00" and ct <= "16:00":
#     print("GA ")
# elif ct > "16:00" and ct <= "19:00":
#     print("GE")
# else:
#     print("GN")
   
# #optimized code
# import time
# cut=time.strftime("%H:%M")
# hrs=int(time.strftime("%H"))
# min=int(time.strftime("%M"))
# if 5 < hrs <= 12:
#     print("gm")
# elif 12 < hrs < 16:
#     print("ga")
# elif 16 < hrs < 19:
#     print("ge")
# else:
#     print("gn")
    
# # Q2] Given three inputs that are stored in the variables a, b, and c.
# # You need to print a a times and b b times  in a single line separated by c.
# a = input()
# b = input()
# c = input()
# ca = int(a)
# cb = int(b)
# print((a*ca) + c + (b*cb))


