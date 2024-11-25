class TreeNode:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val
def preorder(head):
    results=[]
    if head is None:
        return results
    results.append(head.val)
    results.extend(preorder(head.left))
    results.extend(preorder(head.right))
    return results
parent = TreeNode(1)
parent.left = TreeNode(2)
parent.right = TreeNode(3)
parent.left.left = TreeNode(4)
parent.left.right = TreeNode(5)
parent.right.left = TreeNode(6)
parent.right.right = TreeNode(7)
print(preorder(parent))