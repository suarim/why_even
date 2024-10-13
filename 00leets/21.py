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

def merge(head1,head2):
    dummy=ListNode(0)
    current=dummy
    while head1 and head2:
        if head1.value<head2.value:
            current.next=head1
            head1=head1.next
        else:
            current.next=head2
            head2=head2.next
        current=current.next
    if head1:
        current.next=head1
    elif head2:
        current.next=head2
    print_linked_list(dummy.next)
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