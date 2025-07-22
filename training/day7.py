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
#     def update_at_pos(self, index, new_data):
#         temp =  self.head
#         count = 0
#         while temp:
#             if count == index:
#                 temp.data = new_data
#                 return
#             temp = temp.next
#             count += 1
#         print("index out of bound")
        
#     def delete_by_value(self,value):
#         temp = self.head
        
#         if temp is None:
#             print("list khali hai")
#             return
#         if temp.data == value:
#             self.head = temp.next
#             self.head = None
#             self.tail = None
            
        
            
# ll=LinkedList()

# ll.insert_end(2)
# ll.insert_end(4)
# ll.insert_end(1)
# ll.insert_end(7)

# ll.insert_beg(0)

# ll.insert_end(9)
# ll.insert_at_pos(0,10)

# ll.display()


#LINKED LIST
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")
        
    def mid(self):
        count = 0
        temp = self.head
        
        while temp:
            count += 1
            temp = temp.next
        
        mid_index = count//2
        s = self.head
        for i in range (mid_index):
            s = s.next
        if s:
            print("middle element is:", s.data)
        else:
            print("list is empty")
            
    def reverse_ll(head):
        prev = None
        current = head
        
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        return prev
        
            
    
        
            
            
            
        


ll = LinkedList()
ll.insert_at_end(9)
ll.insert_at_end(5)
ll.display()
ll.mid()
ll.head = reverse_ll(ll.head)
ll.display()


ll.display

            
        