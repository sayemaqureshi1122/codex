marks = [1,2,3,4]
print(marks)
print(type(marks))
# Range in List
list1 = [1, 2, 3, 4, 56, 6, 7]
print(list1[ : ])
print(list1[2 : ])
print(list1[ : 7])
print(list1[0 : 7 : 3])
print(list1[-3])
print(list1[-7 : -4 : 1])

''' Q1] To print the square of elements of list and store it in another list.'''
list2 = [1,2,3,4]
sqrt = []
for i in list2:
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
for i in range(3):
    row = []
    for j in range(3):
        count += 1
        row.append(count)   
    matrix. append(row)
for row in matrix:
    print(row)
    
''' Q20]Create a list of integers from 1 to 20. Print all even numbers.'''
list3 = []
for i in range(1,21):
    if i % 2 == 0:
        list3.append(i)
print(list3)

''' Q21]Reverse a list without using the reverse() method.'''

arr = [1, 2, 3, 4]
new_list = []
c = len(arr)
# print(c)
for i in range(len(arr)):
    c  = arr[len(arr) - 1]
    new_list.append(c)
    arr.remove(c)
    
print(new_list)


# without any built function
list4 = [1, 2, 3, 4]
count = 0
new = []
#to count the no. of elements subsitute of len()
for i in list4:
    count += 1
# print(count)
b = count - 1
while b >=0:
    val = list4[b]
    temp = []
    for i in new:
        temp += [i]
    temp += [val]
    new = temp    
    b -= 1
    
for val in new:
    print(val)  
    
# with slicing

nums = [1, 2, 3, 4]
reverse = nums[ : : -1]    
print(reverse)

''' Q22]Input 5 student names and store them in a list. Then sort them alphabetically.'''
names = []
for i in range(5):
    name = input("enter a name:")
    names. append(name)
print(names)
names.sort()
print(names)

''' Q23]Remove all occurrences of a specific element from a list (e.g., remove all 0s).'''
list5 = [1, 3, 4, 0]
for i in list5:
    if i == 0:
        list5.remove(i) 
print(list5)

''' Q24]Find the second largest number in a list of integers.'''
list6 = [1, 3, 5, 809, 0, 6]
list6.sort()
print(list6)
print(list6[len(list6) - 2])

''' Q 25] Create a tuple with 5 elements. Print the last element using negative indexing.'''
tup = (1, 2, 3, 4, 5)
print(tup[-1])

''' Q26] Check if an element exists in a tuple.'''
tup1 = (1, 2, 3, 0, 5)
if 3 in tup:
    print("yes there is 3 in the tuple")
    
''' Q27] Convert a tuple into a list and add a new element to it.'''
tup2 = ("sam", "ram", "thor")
print(tup2)
c = list(tup2) #converting tuple into list
print(c) 
c.append("caption")
d = tuple(c) #back into a tuple
print(d)

'''Q28] Swap the first and last elements of a tuple'''
tup3 = (10, 20, 30, 40)
tup31 =(tup3[ : : -1]) #always use slicing in tuple u cannot use append and remove wala logic unless u covert this tuple into a list
print(tup31)

''' Q29] KBC'''
print("Sawagt hai apka KBC mai hu ABMITABH Bacchan apke sath")
input()
print("Chaleye shuru karte hai")
print("Kya aap khel ke liye tayar hai? to enter dabaye")
input()
print("shru karte hai Vidusho ji apka sawal 100 rupay ke liye ye raha apke computer screen pe:")
amt = 0
list7 = ["Apke best Friend ko Gussa  apke konse dost ko dekh ke ata hai? \n1]Shafain \n2]Soumitra \n3]Tushar \n4]vedant"]
for i in list7:
    print(i)
ans1  = input("ans:")
if ans1 == "3":
    print("Bilkul sahi jawab hai apka \n Aap jit chuke hai 100 rupay")
    amt += 100
    print("chalte hai next question pe..")
    print("ye raha apke computer screen pe 250 rupay ke liye")
    list8 = ["Q2]Apke best friend ka Zodiac sign kya hai \n1]Scropio \n2]Libra\n3]Gemini\n 4]Aries"]
    for i in list8:
        print(i)
    ans2 = input("ans:")
    if ans2 == "3":
        print("sahi jawab isse ke sath aap jit chuke hai 350 rupay")
        amt += 250
        list9 = ["Q3] My one interaction with someone u do not like \n1]Soumitra \n2]Komal \n3]Yash \n4]Sejal"]
        for i in list9:
            print(i)
        ans3  = input("ans:")
        if ans3 == "2":
            amt += 500
            print("bilkul sahi jawab")
        else:
            print("galat jawab")
    else:
        print("galat jawab")
else:
    print("galat jawab")
print(f"isse ke sath aap jit chuke hai pure {amt} rupay")

questions = [["fav colour","blue", "pink", "black", "brown"], ["fav food", "pizza", "burger", "pasta","maggie"]]
ans = ["c", "d"]
amt = 0
level = [100, 200]
for i in range(len(questions)):
    print(f"question for {level[i]} rupees")
    print(questions[i][0])
    print(f"a. {questions[i][1]}            b.  {questions[i][2]}")
    print(f"c. {questions[i][3]}            d.  {questions[i][4]}")
    ans1 = input("enter our opt: ")
    if ans1 == ans[i]:
        print("correct ans")
        amt += level[i]
    else:
        print("wrong")
        break
print(f"You have won {amt} rupees Congo")
