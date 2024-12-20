class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def add(head, x):
    y = ListNode(x)
    while head.next:
        head = head.next
    head.next = y

def rem(head):
    if head.next:
        while head.next.next:
            head = head.next
        head.next = None

def peek(head):
    while head.next:
        head = head.next
    return head.val

def prints(head):
    head = head.next
    while head:
        print(head.val, end="-->")
        head = head.next
    print("None")

head = ListNode(0)
add(head, 1)
add(head, 2
    )
add(head, 3)
add(head, 4)
prints(head)
