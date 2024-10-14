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

def swap_pairs(head):
    dummy=ListNode(0)
    dummy.next=head 
    prev,cur=dummy,head
    while cur and cur.next:
        nxt=cur.next.next
        second=cur.next
        cur.next=nxt
        second.next=cur
        prev.next=second
        prev=cur
        cur=nxt
    return dummy.next

def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")

list1_values = [1,2,3,4,5]

list1 = create_sorted_linked_list(list1_values)
print("List 1:")
print_linked_list(list1)
print("Swapped List:")
swap_pairs2 = swap_pairs(list1)
print_linked_list(swap_pairs2)


