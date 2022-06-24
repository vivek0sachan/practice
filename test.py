from distutils.log import debug
from hashlib import new


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Linked_list:
    def __init__(self):
        self.head=None

    def traverse(self,position):
        current=self.head
        if position==1:
            return self.head
        else:
            for i in range(position-1):
                if current is None:
                    return ('position exceeds limit')
                current=current.next
            return current
            
            # insert after given node
    def insert_after(self,previous_node,data):
        new_node=Node(data)
        new_node.next=previous_node.next
        previous_node.next=new_node

        #push data

    def push(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node




if __name__=='__main__':
    l_list=Linked_list()
    head_node=Node(12)
    head_node.data=12
    print (head_node.data)
    second=Node(22)
    third=Node(33)
    l_list.head=head_node
    head_node.next=second
    second.next=third
    print (head_node.data)
    print(l_list.traverse(3).data)
    
    
    #traversing linked_list
