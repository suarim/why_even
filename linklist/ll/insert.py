class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None
def prints(head):
    cur=head
    while cur:
        print(cur.val,end=" -> ")
        cur=cur.next
    print("None")
def insert(head,data):
    cur=head
    while cur.next:
        cur=cur.next
    cur.next=ListNode(data)
head=ListNode(1)
head.next=ListNode(2)
head.next.next=ListNode(3)
head.next.next.next=ListNode(4)
prints(head)
insert(head,5)
prints(head)
