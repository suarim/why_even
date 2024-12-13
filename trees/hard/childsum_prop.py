

class TreeNode:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val

def childsum_prop(root):
    c=0
    if not root:
        return 
    if root.left:
        c+=root.left.val
    if root.right:
        c+=root.right.val
    if c<root.val:
        if root.left:
            root.left.val=root.val
        if root.right:
            root.right.val=root.val
    else:
        root.val=c
    childsum_prop(root.left)
    childsum_prop(root.right)
    tot=0
    if root.left:
        tot+=root.left.val
    if root.right:
        tot+=root.right.val
    if root.left or root.right:
        root.val=tot
    return root
def printtree(root):
    if not root:
        return
    printtree(root.left)
    print(root.val)
    printtree(root.right)
parent = TreeNode(1)
parent.left = TreeNode(2)
parent.right = TreeNode(3)
parent.left.left = TreeNode(4)
parent.left.right = TreeNode(5)
parent.right.left = TreeNode(6)
parent.right.right = TreeNode(7)
printtree(childsum_prop(parent))