class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None
def prints(head):
    cur = head
    while cur:
        print(cur.val, end=" -> ")
        cur = cur.next
    print("None")
def is_palindrome_1(head):
    l=[]
    while head:
        l.append(head.val)
        head=head.next
    return l==l[::-1]
def reverse(head):
    prev=None
    cur=head
    while cur:
        nxt=cur.next
        cur.next=prev
        prev=cur
        cur=nxt
    return prev
def is_palindrome_2(head):
    fast=slow=head
    while fast and fast.next:
        fast=fast.next.next
        slow=slow.next
    slow=reverse(slow)
    fast=head
    while slow:
        if slow.val!=fast.val:
            return False
        slow=slow.next
        fast=fast.next
    return True

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(2)
head.next.next.next.next = ListNode(1)
prints(head)
print(is_palindrome_1(head))
print(is_palindrome_2(head))