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

def dele(head,key):
    temp=head
    while temp.right:
        if temp.val==key:
            if temp.left:
                temp.left.right=temp.right
            if temp.right:
                temp.right.left=temp.left
            if temp==head:
                head=temp.right
            
        temp=temp.right
    return head
head=ListNode(1)
head.right=ListNode(2)
head.right.left=head
head.right.right=ListNode(2)
head.right.right.left=head.right
head.right.right.right=ListNode(3)
head.right.right.right.left=head.right.right
head.right.right.right.right=ListNode(4)
head.right.right.right.right.left=head.right.right.right
prints(head)
prints(dele(head,2))
