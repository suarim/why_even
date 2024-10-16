class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
def prints(head):
    cur=head
    while cur:
        print(cur.val,end=" -> ")
        cur=cur.next
    print("None")
def del_tail(head):
    cur=head
    while cur.next.next:
        cur=cur.next
    cur.next=None
    return head
head=ListNode(1)
head.next=ListNode(2)
head.next.next=ListNode(3)
head.next.next.next=ListNode(4)
del_tail(head) 
del_tail(head) 
prints(head)