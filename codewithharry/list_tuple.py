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

