class Node:
    def __init__(self,data):
        self.data=None
        self.next=None

class Linked_list:
    def __init__(self):
        self.head=None

if __name__=='__main__':
    l_list=Linked_list()
    head_node=Node(1)
    second=Node(22)
    third=Node(33)
    l_list.head=head_node
    head_node.next=second
    second.next=third

    #traversing linked_list