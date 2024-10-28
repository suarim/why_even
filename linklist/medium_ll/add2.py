class ListNode():
    def __init__(self,x):
        self.val=x
        self.next=None
def prints(head):
    cur=head
    while cur:
        print(cur.val,end=" -> ")
        cur=cur.next
    print("None")

def add2linkedlists(l1, l2):
    carry = 0
    dummy = ListNode(0)
    current = dummy
    while l1 or l2 or carry:
        lv1 = l1.val if l1 else 0
        lv2 = l2.val if l2 else 0
        sum = lv1 + lv2 + carry
        carry = sum // 10
        current.next = ListNode(sum % 10)
        current = current.next
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
    return dummy.next


head1=ListNode(1)
head1.next=ListNode(2)
head1.next.next=ListNode(3)
head2=ListNode(4)
head2.next=ListNode(5)
head2.next.next=ListNode(6)
prints(add2linkedlists(head1,head2))