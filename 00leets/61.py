class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

def rotate(head,k):
    cur=head
    x=head
    len=1
    while cur.next:
        len+=1
        cur=cur.next
    cur.next=head
    print(len)
    k=k%len
    p=1
    while p!=len-k:
        p+=1
        x=x.next
    z=x.next
    x.next=None
    return z



# Create a linked list and append 5 elements
llist = LinkedList()
elements = [1, 2, 3, 4, 5]
for elem in elements:
    llist.append(elem)

# Print the linked list
llist.print_list()
llist.head = rotate(llist.head, 2)
llist.print_list()