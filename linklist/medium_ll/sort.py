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

    if not head:
        return head
    slow=head
    fast=head
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
    return slow
def merge(left,right):
    dummy=ListNode(0)
    cur=dummy
    while left and right:
        if left.val<right.val:
            cur.next=left
            left=left.next
        else:
            cur.next=right
            right=right.next
        cur=cur.next
    if left:
        cur.next=left
    if right:
        cur.next=right
    return dummy.next
def mergesort(head):
    if not head or not head.next:
        return head
    prev=None
    slow=head
    fast=head
    while fast and fast.next:
        prev=slow
        slow=slow.next
        fast=fast.next.next
    prev.next=None
    left=mergesort(head)
    right=mergesort(slow)
    return merge(left,right)
    
head=ListNode(5)
head.next=ListNode(4)
head.next.next=ListNode(3)
head.next.next.next=ListNode(2)
head.next.next.next.next=ListNode(1)
prints(head)
prints(mergesort(head))
