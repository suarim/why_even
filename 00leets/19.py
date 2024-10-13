class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data, end=" -> ")
            cur_node = cur_node.next
        print("None")



def removeNthFromEnd(head, n):
    cur=head
    l=0
    while cur:
        l+=1
        cur=cur.next
    print(l)
    from_begin=l-n+1
    z=from_begin
    #z=4
    cur=head
    p=1
    while cur :
        if p+1==z:
            cur.next=cur.next.next
            break
        p+=1
        cur=cur.next
    
    



# Example usage:
if __name__ == "__main__":
    llist = LinkedList()
    llist.append(1)
    llist.append(2)
    llist.append(3)
    llist.append(4)
    llist.append(5)
    llist.print_list()
    removeNthFromEnd(llist.head, 4)
    llist.print_list()