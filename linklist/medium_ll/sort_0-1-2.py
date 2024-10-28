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
def sorts(head):
    dummy0=ListNode(0)
    dummy1=ListNode(0)
    dummy2=ListNode(0)
    cur0=dummy0
    cur1=dummy1
    cur2=dummy2
    cur=head
    while cur:
        if cur.val==0:
            cur0.next=cur
            cur0=cur0.next
        elif cur.val==1:
            cur1.next=cur
            cur1=cur1.next
        else:
            cur2.next=cur
            cur2=cur2.next
        cur=cur.next
    cur0.next=dummy1.next
    cur1.next=dummy2.next
    return dummy0.next

head=ListNode(1)
head.next=ListNode(0)
head.next.next=ListNode(2)
head.next.next.next=ListNode(1)
head.next.next.next.next=ListNode(0)
head.next.next.next.next.next=ListNode(2)
head.next.next.next.next.next.next=ListNode(1)
head.next.next.next.next.next.next.next=ListNode(0)
head.next.next.next.next.next.next.next.next=ListNode(2)
head.next.next.next.next.next.next.next.next.next=ListNode(2)
prints(sorts(head))