class TreeNode:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val
def height(head):
    if not head:
        return 0
    lh=height(head.left)
    rh=height(head.right)
    return 1+max(lh,rh)

parent = TreeNode(1)
parent.left = TreeNode(2)
parent.right = TreeNode(3)
parent.left.left = TreeNode(4)
parent.left.right = TreeNode(5)
parent.right.left = TreeNode(6)
parent.right.right = TreeNode(7)
print(height(parent))
