class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def prints(head):
    cur = head
    while cur:
        print(cur.val, end=" -> ")
        cur = cur.next
    print("None")
def removeNthFromEnd(head, n):
    cur=head
    l=0
    while cur:
        l+=1
        cur=cur.next
    print(l)
    from_begin=l-n+1
    z=from_begin
    #z=4
    cur=head
    p=1
    while cur :
        if p+1==z:
            cur.next=cur.next.next
            break
        p+=1
        cur=cur.next
    return head
    
    
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
prints(removeNthFromEnd(head, 2))