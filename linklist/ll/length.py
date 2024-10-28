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
def length(head):
    cur=head
    len=0
    while cur:
        len+=1
        cur=cur.next
    return len
head=ListNode(1)
head.next=ListNode(2)
head.next.next=ListNode(3)
head.next.next.next=ListNode(4)
print(length(head))