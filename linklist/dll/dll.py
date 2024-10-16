class ListNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
def prints(head):
    cur = head
    while cur:
        print(cur.val, end=" -> ")
        cur = cur.right
    print("None")
head = ListNode(1)
head.right = ListNode(2)
head.right.left = head
head.right.right = ListNode(3)
head.right.right.left = head.right
prints(head)
