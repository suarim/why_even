class TreeNode:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val
def isSymmetric(root):
    def sym(first,second):
        if not first and not second:
            return True
        if not first or not second:
            return False
        if first.val!=second.val:    
            return False
        return sym(first.left,second.right) and sym(first.right,second.left)
    return sym(root,root)
parent = TreeNode(1)
parent.left = TreeNode(2)
parent.right = TreeNode(2)
parent.left.left = TreeNode(3)
parent.left.right = TreeNode(4)
parent.right.left = TreeNode(4)
parent.right.right = TreeNode(3)
print(isSymmetric(parent))