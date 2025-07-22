'''
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
result = fibonacci(6)
print(result)

#sum of natural numbers
def sum_of_natural_no(n):
    if n == 0:
        return 0
    else:
        return n+sum_of_natural_no(n-1)
res=sum_of_natural_no(4)
print(res)

#sum of digits
def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return n%10 + sum_of_digits(n//10)
res=sum_of_digits(1224)
print(res)

#reverse the string
def rev_str(s):
    if len(s) == 0:
        return s
    else:
        return rev_str(s[1:])+s[0]
res = rev_str("hello")
print(res)

#tower of hanoi    
def tower_of_hanoi(n, source, auxiliary, destination):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    # Step 1: Move top (n-1) disks from source to auxiliary
    tower_of_hanoi(n - 1, source, destination, auxiliary)
    
    # Step 2: Move the largest disk to destination
    print(f"Move disk {n} from {source} to {destination}")
    
    # Step 3: Move the (n-1) disks from auxiliary to destination
    tower_of_hanoi(n - 1, auxiliary, source, destination)

# Example: Solve for 3 disks
tower_of_hanoi(3, 'A', 'B', 'C')

#count zeroes in a number

#replace all "pi" with "3.14" in a string
def replace_pi(s):
    
    if len(s) <=1:
        return s
    if s[:2] == "pi":
        return "3.14" + replace_pi(s[2:])
    return s[0] + replace_pi(s[1:])

# Example usage:
text = "hipi"
result = replace_pi(text)
print(result)
'''
# power of 2 return true if not false
def power(n):
    if n == 1:
        return True
    elif n == 0 or n%2 !=0:
        return False
    else:
        return power(n//2)
res= power(24)
print(res)
   
# convert a non-negative integer num to its english words representation.
def num_to_words(n):
    if n == 0:
        return "zero"
    below_20=["",'one','two','three','four','five', 'six', 'seven', 'eight','nine', 'ten','eleven','twelve', 'thirteen', 'fourteen','fifteen', 'sixteen','seventeen', 'eighteen','nineteen']
    tens=['','', 'twenty','thirty','forty','fifty','sixty', 'seventy', 'eighty', 'ninety']
    units=['','','thousand','million','billions']
    
    def helper(x):
        word=""
        if n<20:
            word += below_20[n%10]
    


#list
list1 = [1,2,3,4]
print(list1)
# using constructor
res=list(("apple","mango"))
print(res)

#slicing
print(list1[:2])
print(list1[1:4])
print(list1[1:4:2])
print(list1[::-1])
print(list1[-3:-1])
print(list1[-2:])
print(list1[:1:-1])
print(list1[::2])# selects every second element from the start
print(list1[1::3]) #with 1st selects every 3rd element

#list comprehension [expression for item in iterable if condition]

#create a list of squares for numbers from 1 to 5 for even number
squares=[x**2 for x in range(1,6) if x%2==0]
print(squares)

#create a upper case char from string
chars=[char.upper() for char in "hello"]
print(chars)

#nested loop

#generate a list pf pairs(x,y) where x is from 1 to 3 amd y from 4 to 6.
pairs=[(x,y) for x in range (1,4) for y in range(4,7)]
print(pairs)

#flattening the array
matrix=[[1,2],[2,3],[3,4]]
flat=[num for row in matrix for num in row]
print(flat)

#create a list of even or odd labels for number 1 to5
labels=["even" if x%2 ==0 else "odd" for x in range(1,6)]
print(labels)


#using function
def sq(n):
    return n*n
sqs=[sq(x) for x in range(1,6)]

