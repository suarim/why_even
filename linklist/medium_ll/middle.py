class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
def prints(head):
    cur = head
    while cur:
        print(cur.val, end=" -> ")
        cur = cur.next
    print("None")
def middle(head):
    fast = slow = head
    while fast and fast.next:
        fast=fast.next.next
        slow=slow.next
    return slow
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
prints(head)
middle_node = middle(head)
print(middle_node.val)