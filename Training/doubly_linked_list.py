# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
    

# class LinkedList:
#     def __init__(self):
#         self.head=None
#         self.tail=None
        
        
#     def insert_end(self,data):
#         new_node = Node(data)
        
#         if not self.head:
#             self.head=new_node
#             self.tail=new_node
            
#         self.tail.next=new_node
#         self.tail=new_node
        
    
#     def insert_beg(self,data):
#         new_node=Node(data)
        
#         new_node.next=self.head
#         self.head=new_node
        
#         if self.tail is None:
#             self.tail=new_node
        
    
#     def display(self):
#         temp=self.head
        
#         while temp:
#             print(temp.data,end=" -> ")
#             temp=temp.next
            
#         print("None")
        
#     def insert_at_pos(self,index,data):
#             if index < 0:
#                 print("Andha hai kya")
#                 return
            
#             if index==0:
#                 self.insert_beg(data)
            
#             new_node=Node(data)
#             temp=self.head
            
#             for i in range (index-1):
#                 if(temp.next==None):
#                     print("Index out of bound")
#                     return 
#                 temp=temp.next
                
            
#             new_node.next=temp.next
#             temp.next=new_node
            
#     def update_at(self,index,new_data):
#             temp=self.head
#             count=0
    
#             while temp:
#                 if count == index:
#                     temp.data=new_data
#                     return 
                
#                 temp=temp.next
#                 count+=1
        
#             print("index out of bound")
            
            
            
            
        
        
#     def delete_by_value(self,value):
#         temp=self.head
        
#         if temp is None:
#             print("List khali hai bhai")
#             return
        
#         if temp.data==value:
#             self.head=temp.next
#             if self.head==None:
#                 self.tail=None
#             return
        
#         prev=None
        
#         while temp and temp.data != value:
#             prev=temp
#             temp=temp.next
            
#             if not temp:
#                 print("value not found")
            
#             if(temp.data==value):
#                 prev.next=temp.next
            
#             if prev.next is None:
#                 self.tail=prev
    
    
#     def delete_at(self,index):
#         if index<0:
#             print("Andha hai kya")
#             return
        
#         temp=self.head
        
#         if index==1:
#             self.head=temp.next
            
#             if self.head is None:
#                 self.tail=None
#             return
        
#         for i in range(1,index-1):
#             if not temp:
#                 print("Index out of bounds")
#                 return
            
#             temp=temp.next
            
#             if not temp or not temp.next:
#                 print("index out of bound")
#                 return
            
#             if temp.next is None:
#                 self.tail=temp
        
#         temp.next=temp.next.next
            
            
        


# ll=LinkedList()

# ll.insert_end(2)
# ll.insert_end(4)
# ll.insert_end(1)
# ll.insert_end(7)

# ll.insert_beg(0)

# ll.insert_end(9)

# ll.insert_at_pos(6,20)

# ll.display()


# ll.delete_by_value(7)

# ll.display()

# ll.delete_at(9)

# ll.display()

class Node :
    def __init__(self,data):
        self.data = data 
        self.next =  None
class LinkedList:
    def __init__(self):
        self.head =None
        self.tail = None
    def insert_at_beg(self,data):
        node1 = Node(data)
        temp = self.head
        
        node1.next = temp
        temp = node1
        
        if temp is None:
            self.head= node1
    def display(self):
        temp = self.head
        while temp :
            print(temp.next, end ="->")
            temp = temp.next
        print("Null")
        
       
ll = LinkedList()
ll.insert_at_beg(90)
ll.display()

