class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
def prints(head):
    while head:
        print(head.val, end='->')
        head = head.next
    print('None')
def deldup(head):
    dummy=ListNode(0)
    dummy.next=head
    rev1=dummy
    prev=head
    cur=head.next
    while cur:
        if prev.val==cur.val:
            nxt=cur.next
            prev.next=nxt
            cur=nxt
        else:
            prev=prev.next
            cur=cur.next
    return dummy.next

head = ListNode(1)
head.next = ListNode(1)
head.next.next = ListNode(2)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(3)
head.next.next.next.next.next = ListNode(4)
prints(head)
prints(deldup(head))