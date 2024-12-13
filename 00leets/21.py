class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def create_sorted_linked_list(values):
    if not values:
        return None
    values.sort()
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")

def merge(l1,l2):
    dummy=ListNode(0)
    curr=dummy
    while l1 and l2:
        if l1.value<l2.value:
            curr.next=l1
            l1=l1.next
        else:
            curr.next=l2
            l2=l2.next
        curr=curr.next
    if l1:
        curr.next=l1
    if l2:
        curr.next=l2
    return dummy.next

# Example usage:
list1_values = [1, 3, 5, 7]
list2_values = [2, 4, 6, 8]

list1 = create_sorted_linked_list(list1_values)
list2 = create_sorted_linked_list(list2_values)

print("List 1:")
print_linked_list(list1)

print("List 2:")
print_linked_list(list2)

merged_list = merge(list1, list2)
print("Merged List:")
print_linked_list(merged_list)