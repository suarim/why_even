class TreeNode:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val
def inorder(head):
    results=[]
    if head is None:
        return results
    results.extend(inorder(head.left))
    results.append(head.val)
    results.extend(inorder(head.right))
    return results
parent = TreeNode(1)
parent.left = TreeNode(2)
parent.right = TreeNode(3)
parent.left.left = TreeNode(4)
parent.left.right = TreeNode(5)
parent.right.left = TreeNode(6)
parent.right.right = TreeNode(7)
print(inorder(parent))