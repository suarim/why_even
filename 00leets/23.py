class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        if not lists:
            return None
        if len(lists)==1:
            return lists[0]
        while len(lists)>1:
            merged=[]
            for i in range(0,len(lists),2):
                l1=lists[i]
                l2=lists[i+1] if i+1<len(lists) else None
                merged.append(self.merge(l1,l2))
            lists=merged
            return lists[0]
    def merge(self,l1,l2):
        dummy=ListNode(0)
        current=dummy
        while l1 and l2:
            if l1.val<l2.val:
                current.next=l1
                l1=l1.next
            else:
                current.next=l2
                l2=l2.next
            current=current.next
        if l1:
            current.next=l1
        if l2:
            current.next=l2
        return dummy.next

def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to print the linked list
def print_linked_list(node):
    result = []
    while node:
        result.append(str(node.val))
        node = node.next
    print(" -> ".join(result))

# Test case
def test_case():
    # Create some sorted linked lists
    list1 = create_linked_list([1, 4, 5])
    list2 = create_linked_list([1, 3, 4])
    list3 = create_linked_list([2, 6])

    # List of all lists
    lists = [list1, list2, list3]

    # Create a solution instance and merge the lists
    solution = Solution()
    merged_list = solution.mergeKLists(lists)

    # Print the merged list
    print("Merged list:")
    print_linked_list(merged_list)

# Run the test case
test_case()