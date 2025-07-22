'''
#print table

for i in range(1,5):
    for j in range(1,5):
        print(i*j ,end= "\t")
    print()       

 #range
for i in range(3):
     print(i)     
    
for i in range(2,5):
    print(i)
#(start, end, step)  can also be -ve
for i in range(1,5,2):
    print(i)
    
for fruit in['a,b,c']:
    print(fruit)
# to print a matrix 
arr=[[1,2,3],[4,5,6]]
for row in arr:
    print(row)

n=5
while n>5:
    print(n)
    
#reverse a number 
num=1234
rem=0
while num > 0:
    digit = num % 10          
    rem = rem * 10 + digit    
    num = num // 10          
print(rem)
if n== rem:
    print(num "and" rem "are palindrome")

year=2024
if (year%4 ==0 and year%100 !=0) or (year%400==0):
    print(year, " is a leap year")
else:
    print( year,"not a leap year")
'''
'''
#use the break statement to stop the loop if user enters -ve number
while True:
    n=int(input())
    if n>0:
        break
    else:
        print(n)


#generate all prime number between  1 to 50

#armstrong number

n=153
digit=0
res=0
new=n
while n>=0:
    digit=n%10
    res += digit*digit*digit
    n/10

# to find the gcd
a=13
b=26
gcd=0
for i in range(1,min(a,b)+1):
    if a%i==0 and b%i==0:
        gcd=i
print(gcd) 


#pattern printing
rows=5
for i in range(1,rows+1):
    print("*"*i)

# inverse pattern
n=4
for i in range(n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for l in range(2*i-1):
        print("*", end=" ")
    print()
    
name= input()
print()

n=5
for i in range(n):
    for j in range(n):
        if(i==0 or i==n-1 or j==0 or j==n-1):
            print("*" , end="")
        else:
            print(" ", end="")
    print()
   
n = 5    
for i in range(n):
    for j in range(i + 1):  
        if i == n - 1 or j == 0 or j == i:
            print("*", end="")
        else:
            print(" ", end="")
    print()



def myfun(*argv):
      for arg in argv:
          print(arg) 
           
myfun("hello", 'welcome', 'to','nagpur')      

def urfun(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}={value}")
        
urfun(name='alice',age=25, city='ngp')
  

res=lambda x:x*x
sq=res(3)
print(sq)


ana= lambda x: x+3
res=ana(9)
print(res)
'''

num=10
for num in range(0,num):
    num +=1
    print(num)
