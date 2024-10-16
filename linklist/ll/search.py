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
def search(head,data):
    cur=head
    while cur:
        if cur.val==data:
            return True
        cur=cur.next
    return False
head=ListNode(1)
head.next=ListNode(2)
head.next.next=ListNode(3)
head.next.next.next=ListNode(4)
print(search(head,9))