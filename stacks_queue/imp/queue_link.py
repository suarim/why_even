class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
def add(head,x):
    y=ListNode(x)
    if head.next:
        z=head.next
        head.next=y
        y.next=z
        return head.next
    else:
        head.next=y
        return head.next
def prints(dummy):
    dummy=dummy.next
    while dummy:
        print(dummy.val,end="-->")
        dummy=dummy.next
    print("None")
def rem(dummy):
    
    if dummy.next:
        x=dummy.next
        while dummy.next.next:
            dummy=dummy.next
        dummy.next=None
        return x
    else:
        return None
def peek(dummy):
    while dummy.next:
        dummy=dummy.next
    return dummy.val
dummy=ListNode(0)
prints(dummy)
add(dummy,1)
prints(dummy)
rem(dummy)
prints(dummy)
add(dummy,2)
add(dummy,3)
prints(dummy)
rem(dummy)
prints(dummy)
rem(dummy)
prints(dummy)
rem(dummy)
prints(dummy)
add(dummy,4)
print(peek(dummy))