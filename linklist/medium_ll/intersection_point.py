class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None
        self.count=0
def prints(head):
    cur = head
    while cur:
        print(cur.val, end=" -> ")
        cur = cur.next
    print("None")
def intersection(head1,head2):
    cur1=head1
    cur2=head2
    while cur1:
        cur1.count+=1
        cur1=cur1.next
    while cur2:
        if cur2.count>0:
            return cur2.val
        cur2=cur2.next
    return -1
head=ListNode(1)
head.next=ListNode(2)
head.next.next=ListNode(3)
head.next.next.next=ListNode(4)
head.next.next.next.next=ListNode(5)
head2=ListNode(6)
head2.next=head.next.next
print(intersection(head,head2))