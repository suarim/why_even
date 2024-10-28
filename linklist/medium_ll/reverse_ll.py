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
def reverse(head):
    prev=None
    cur=head
    while cur:
        nxt=cur.next
        cur.next=prev
        prev=cur
        cur=nxt
    return prev
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
prints(head)
prints(reverse(head))