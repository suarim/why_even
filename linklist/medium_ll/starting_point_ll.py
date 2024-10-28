class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.count = 1
def prints(head):
    cur = head
    while cur:
        print(cur.val, end=" -> ")
        cur = cur.next
    print("None")
def starting(head):
    cur=head
    while cur.next:
        cur.count+=1
        if cur.count>2:
            return cur
        cur=cur.next
    return head
head=ListNode(1)
head.next=ListNode(2)
head.next.next=ListNode(3)
head.next.next.next=ListNode(4)
head.next.next.next.next=ListNode(5)
head.next.next.next.next.next=head.next
print(starting(head).val)