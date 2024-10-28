class ListNode:
    def __init__(self, x):
        self.val = x
        self.right = None
        self.left = None
def prints(head):   
    cur = head
    while cur:
        print(cur.val, end=" -> ")
        cur = cur.right
    print("None")
def rem_depl(head):
    prev=head
    cur=head.right
    while cur:
        if cur.left and cur.val==cur.left.val:
            prev.right=cur.right
            if cur.right:
                cur.right.left=prev
            cur=prev.right
        else:
            prev=cur
            cur=cur.right
        
    return head
head=ListNode(1)
head.right=ListNode(1)
head.right.left=head
head.right.right=ListNode(2)
head.right.right.left=head.right
head.right.right.right=ListNode(2)
head.right.right.right.left=head.right.right
head.right.right.right.right=ListNode(3)
head.right.right.right.right.left=head.right.right.right
prints(rem_depl(head))
