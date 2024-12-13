class TreeNode:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val

def lca(root,n1,n2):
    if root is None or root.val==n1 or root.val==n2:
        return root
    left=lca(root.left,n1,n2)
    right=lca(root.right,n1,n2)
    if not left:
        return right
    elif not right:
        return left
    else:
        return root
parent = TreeNode(1)
parent.left = TreeNode(2)
parent.right = TreeNode(3)
parent.left.left = TreeNode(4)
parent.left.right = TreeNode(5)
parent.right.left = TreeNode(6)
parent.right.right = TreeNode(7)
print(lca(parent,3,5).val)