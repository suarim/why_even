class TreeNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

maxi = 0  

def maxh(root):
    global maxi
    if root is None:
        return 0
    lh = maxh(root.left) 
    rh = maxh(root.right)
    maxi = max(maxi, lh + rh) 
    return 1 + max(lh, rh)
def diameter(root):
    global maxi
    if not root:
        return 0
    maxi = 0 
    maxh(root)  
    return maxi  


parent = TreeNode(1)
parent.left = TreeNode(2)
parent.right = TreeNode(3)
parent.left.left = TreeNode(4)
parent.left.right = TreeNode(5)
parent.right.left = TreeNode(6)
parent.right.right = TreeNode(7)

print(diameter(parent))
