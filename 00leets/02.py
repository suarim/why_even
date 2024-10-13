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
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


def add2linkedlists(l1, l2):
    carry = 0
    dummy = Node(0)
    current = dummy
    while l1 or l2 or carry:
        lv1 = l1.data if l1 else 0
        lv2 = l2.data if l2 else 0
        sum = lv1 + lv2 + carry
        carry = sum // 10
        current.next = Node(sum % 10)
        current = current.next
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
    return dummy.next

# Function to print the resulting linked list after adding
def print_linked_list(node):
    while node:
        print(node.data, end=" -> ")
        node = node.next
    print("None")


# Create first linked list
list1 = LinkedList()
list1.append(2)
list1.append(4)
list1.append(3)

# Create second linked list
list2 = LinkedList()
list2.append(5)
list2.append(6)
list2.append(4)

# Print both linked lists
print("First linked list:")
list1.print_list()

print("Second linked list:")
list2.print_list()

# Use the function to add the two linked lists
result = add2linkedlists(list1.head, list2.head)

# Print the resulting linked list
print("Resultant linked list after addition:")
print_linked_list(result)
