#print triangle pattern
row=int(input("enter number of rows"))
# for i in range(1,row+1):
#     print("*"*i)
    
#print mirror triangle pattern
for i in range(1,row+1):
        print(" "*(row-i) + "*"*i)

#ARRAY
arr = [1,2,3,4]
sum = 0
for i in arr:
    sum += i
print(sum)
avg = sum / len(arr)
print(avg)
#or taking arr as in input
arr = []
sum=0
print("print 5 numbers: ")
for i in range(5):
    num=int(input(f"enter number{i}: "))
    arr.append(num)
print(arr)
for i in arr:
    sum += i
print("sum of array:",sum)
avg=sum/5
print(avg)

#to print table
t=int(input("enter a number: "))
print(f"to print table of {t}")
for i in range(1,11):
    print(f"{t} X {i} = {t*i}")
    
# a=4
# n= []
# for i in range(4):
#     num=int(input(f"enter first element of an array"))
#     n.append(num)
# print(n)
# # n=[12,34,5,65]
# # a=int(input("value:"))
# found = False
# for i in range(0,len(n)):
#     if n[i] == a:
#         print(f"the number is in the array on {i} position")
#         found = True
#         break 
# if not found:
#     print("number is not present in an array")
    
#orrr

# def search(arr,target,length):
#     for i in range(0,length):
#         if (arr[i]==target):
#             return i
#     return -1
# arr=[3,7,1,2,3]
# target=12
# length=int(len(arr))

# #binary search
# target=5
# arr=[1,2,3,4]
# start=0
# end= len(arr)-1
# print(end)
# while start <= end:
#     mid=(start+end)//2
#     if arr[mid] == target:
#         print(f"target found at {mid} position")
#         break
#     elif arr[mid] < target:
#         start = mid + 1
#     else:
#         end = mid - 1
# else:
#     print("target not found")
    
# #using function
# def search_number(arr, target):
#     found = False
#     for i in range(len(arr)):
#         if arr[i] == target:
#             print(f"The number is in the array at index {i}")
#             found = True
#             break
#     if not found:
#         print("Number is not present in the array.")

# # Input list and target value
# n = [12, 34, 5, 65]
# a = int(input("Enter a number to search: "))

# # Call the function
# search_number(n, a)

# #BUBBLE SORT
# def bubble_sort(arr):
    # n = len(arr)
    # for i in range(n):
    #     # Inner loop pushes the largest element to the end
    #     for j in range(0, n - 1 - i):
    #         if arr[j] > arr[j + 1]:
    #             # Swap if current element is greater than the next
    #             arr[j], arr[j + 1] = arr[j + 1], arr[j]

# # Main array
# arr = [3,45,78,2,6]

# print("Before Sorting:", arr)
# bubble_sort(arr)  # This sorts the array in place
# print("After Sorting:", arr)

# # SELECTION SORT
# def selection_sort(arr):
#     n = len(arr)
#     min_index=0
#     for i in range(n-1):
#         min_index=i
#         for j in range (i+1,n):
#             if arr[j] < arr[min_index]:
#                 min_index = j
#         arr[i], arr[min_index] = arr[min_index], arr[i]
# arr=[1,2,6,8,4]
# print(arr)
# selection_sort(arr)
# print(arr)

# def second_largest(arr):
#     n = len(arr)
#     min_index=0
#     for i in range(n-1):
#         min_index=i
#         for j in range (i+1,n):
#             if arr[j] < arr[min_index]:
#                 min_index = j
#         arr[i], arr[min_index] = arr[min_index], arr[i]
# arr =[1,2,6,4,5]
# second_largest(arr)
# print(arr)

arr = [1,2,3,4]
n = len(arr)
max = arr[0]
for i in range (1,n):
    if arr[i] > max:
        max == arr[i]
print(max)

        
         
        
        
