# #to count no of even numbers in an array
# arr=[1,2,3,4,5]
# c=0 
# d=0
# for i in arr:
#      if i%2 == 0:
#          c +=1
#      if i in arr:
#          if i%2 !=0:
#              d+=1
# print(c)
# print(d)

# n=[1,2,3,4]
# for i in n:
#     if i %2 ==0:
#         print("Fizz")
#     if i % 3==0:
#         print("Buzz")
#     if i % 5==0:
#         print("fizzbuzz")
        
        
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

a=1
b=2
c=3
if a > b and a>c:
    print(a)
if b > a and b > c:
    print(b)
if c > a and c > a:
    print(c)
    
year=2000
if (year%4 ==0 and year%100 !=0) or (year%400==0):
    print(year, " is a leap year")
else:
    print( year,"not a leap year")

