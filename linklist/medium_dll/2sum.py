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
def find(head,tail):
    l=set()
    while head and tail and head!=tail:
        s=head.val+tail.val
        if s==5:
            l.add(tuple(sorted([head.val,tail.val])))
            head=head.right
            tail=tail.left
        elif s<5:
            head=head.right
        else:
            tail=tail.left
    return l
head=ListNode(1)
head.right=ListNode(2)
head.right.left=head
head.right.right=ListNode(3)
head.right.right.left=head.right
head.right.right.right=ListNode(4)
head.right.right.right.left=head.right.right
head.right.right.right.right=ListNode(9)
head.right.right.right.right.left=head.right.right.right
tail=head.right.right.right.right
prints(head)
print(find(head,tail))