# def reverse_string(s):
#     a1 = list(s)  
#     left = 0
#     right = len(a1) - 1

#     while left < right:
#         a1[left], a1[right] = a1[right], a1[left]
#         left += 1
#         right -= 1
#     reversed_str = ''.join(a1)
#     print(reversed_str)
# s = "sayema"
# reverse_string(s)


#doubly linked list

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
        
class DoublyLinklist:
    def __init__(self):
        self.head=None
        self.tail=None
        
    def insert_end(self,data):
        new_node = Node(data)
        
        if not self.head:
            self.head=new_node
            return
        
        temp=self.head
            
        while temp.next:
            temp=temp.next
        
        temp.next=new_node
        new_node.prev=temp
        
    def display_for(self):
        temp=self.head
        
        while temp:
            print(temp.data,end=" <=> ")
            temp=temp.next
            
        print("None")
        
    def display_back(self):
        temp=self.head
        
        if not temp:
            print("List is empty")
        
        while temp.next:
            temp=temp.next
        
        while temp:
            print(temp.data,end=" <=> ")
            temp=temp.prev
        
        print("None")
    def insert_at_beg(self,data):
        node1 = Node(data)
        node1.next = self.head
        if self.head:
            self.head.prev = node1
        self.head = node1
    
    def insert_at_part_ind(self, index, data):
        node2 = Node(data)
        temp = self.head
        
        if index < 0:
            print("ulta ja raha hai")
            return
        if index == 0:
            self.insert_at_beg(data)
            return
        temp = self.head 
        for i in range (index-1):
            if not temp:
                print("index out of bound")
                return
            temp = temp.next
            node2.next = temp.next
            node2.prev = temp
            
            if temp.next:
                temp.next.prev = node2
            temp.next = node2
    def delete_by_value(self,value):
        temp =self.head
        t = self.tail
        while temp:
            if temp.data == value:

dll=DoublyLinklist()
dll.insert_at_beg(6)
dll.insert_end(9)
dll.insert_end(8)
# dll.insert_at_part_ind(2,3)
dll.delete_by_value(9)
dll.display_for()
