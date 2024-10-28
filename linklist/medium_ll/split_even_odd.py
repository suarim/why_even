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
def split(head):
    dummy1 = even = ListNode(0)
    dummy = odd = ListNode(0)
    cur=head
    while cur:
        if cur.val%2==0:
            even.next=cur
            even=even.next
        else:
            odd.next=cur
            odd=odd.next
        cur=cur.next
    even.next=dummy.next
    odd.next=None
    prints(dummy.next)
    prints(dummy1.next)
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)
prints(head)
split(head)