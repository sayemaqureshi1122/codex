marks = [1,2,3,4]
print(marks)
print(type(marks))
# Range in List
list = [1, 2, 3, 4, 56, 6, 7]
print(list[ : ])
print(list[2 : ])
print(list[ : 7])
print(list[0 : 7 : 3])
print(list[-3])
print(list[-7 : -4 : 1])

''' Q1] To print the square of elements of list and store it in another list.'''
list = [1,2,3,4]
sqrt = []
for i in list:
    c = i * i
    sqrt.append(c)
print(sqrt)

#USING LIST COMPREHENSION
square = [i * i for i in [1,2,3,4]]
print(square)

''' Q2] To segregate mirchi in another list'''
sabzi = ["aalo", "matar", "mirchi", "haldi", "mirchi", "namak"]

seg  = []
for i in sabzi:
    if i == "mirchi":
        seg.append(i)
print(sabzi)
print(seg)

#usig list comprehension
new_seg = [i for i in sabzi if i == "mirchi"]
print(new_seg)


names = ["milo", "bruno", "anastasia", "sarah", "rose"]  
name_with_o = [names.index(i) for i in names if "o" in i]  
print(name_with_o)

''' Q3]5. List comprehension to create multiplication table for 5'''
new_list = [5 * i for i in range(1, 11)]
print(new_list)

''' Q4] 6. Nested list comprehension example: create pairs (i, j)'''
p = [(i, j) for i in range(3) for j in range(3)]
print(p)

''' Q5] Create a list of 5 favorite fruits. Print the 3rd fruit.'''
fav_fruits = ["apple", "mango", "banana", "strawberry", "kiwi"]
print(fav_fruits[2])

''' Q6] Replace the 2nd item in a list ['a', 'b', 'c'] with 'z'.'''
alph = ['a', 'b', 'c']
alph[2] = 'z'
print(alph)

''' Q7] Add "mango" to the end of the list using a list method.'''
fav_fruits.append("dragonfruit")
print(fav_fruits)

''' Q8] Remove "apple" from this list: ['apple', 'banana', 'cherry']'''
fav_fruits.remove("apple")
print(fav_fruits)

''' Q9] Reverse this list using a method: [1, 2, 3, 4]'''
l1 = [1,2,3,4]
l1.reverse() #never try to print(l1.reverse()) as here the reverse just string ko ulta karta hai kuch return nahi karta isliye op me None likhke ata hai
print(l1)

#OR
l1.sort(reverse = True)
print(l1)

''' Q10]Find the index of "banana" in this list: ['apple', 'banana', 'cherry']'''
print(fav_fruits)
if "banana" in fav_fruits:
    print("it is there in list")
    print(fav_fruits.index("banana"))
    
''' Q11] Count how many times 5 occurs in the list: [1, 5, 5, 2, 5]'''
l2 = [1, 5, 5, 2, 5]
print(l2.count(5))


''' Q12] insert "grape" at index 1 in a list.'''
fav_fruits.insert(0, 'grape')
print(fav_fruits)

''' Q13]Copy a list without using = (use a method).'''
m = fav_fruits.copy()
m[3] = "cherry"
print(m)


''' Q14] Create a list of squares from 0 to 9 using list comprehension.'''
sqrt = [i*i for i in range(10)]
print(sqrt)

''' Q15]From a list of numbers 0 to 19, make a new list of even numbers using list comprehension.'''
even = [i for i in range(20) if i % 2 == 0]
print(even)

''' Q16]Convert a list of temperatures in Celsius to Fahrenheit using list comprehension:[0, 10, 20, 30]'''
fahrenheit = [(i * (9/5)) + 32 for i in [0, 10, 20, 30]]
print(fahrenheit)

''' Q17] From a string "hello world", create a list of vowels using list comprehension.'''
vowels = [i for i in "hello world" if i =="a" or i == "e" or i == "o" or i == "e" or i == "u"]
print(vowels)


'''Q18] Create a list of all numbers from 1 to 50 that are divisible by 3 and 5.'''
num = [i for i in range(51) if i % 3 == 0 and i % 5 == 0]
print(num)

'''Q19] Create a 3x3 matrix of numbers starting from 1 to 9.'''
matrix = []
count = 0
for i in range(2):
    row = [] 
    for j in range(3):
        row.append(count)
        count += 1
    matrix.append(row)
   
for row in matrix:
    print(row)  
    
     
         

