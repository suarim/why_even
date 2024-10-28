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
def reverse(head):
    prev=None
    cur=head
    while cur:
        next=cur.next
        cur.next=prev
        prev=cur
        cur=next
    return prev 
def addOne(head):
    head=reverse(head)
    cur=head
    carry=1
    while cur:
        s=cur.val+carry
        carry=s//10
        cur.val=s%10
        cur=cur.next
    if carry:
        cur=head
        while cur.next:
            cur=cur.next
        cur.next=ListNode(1)
    return reverse(head)
    

head=ListNode(9)
head.next=ListNode(9)
head.next.next=ListNode(9)
head.next.next.next=ListNode(9)
prints(addOne(head))