class TreeNode:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val
def maxh(root):
    if root is None:
        return 0
    return 1+max(maxh(root.left),maxh(root.right))
def balance(root):
    if not root:
        return True
    o1=balance(root.left)
    o2=balance(root.right)
    cond=abs(maxh(root.left)-maxh(root.right))<=1
    if o1 and o2 and cond:
        return True
    return False
def optimax(root):
    if not root:
        return 0
    lh=optimax(root.left)
    rh=optimax(root.right)
    if lh==-1 or rh==-1 or abs(lh-rh)>1:
        return -1
    return 1+max(lh,rh)
def balanceopt(root):
    return optimax(root)!=-1
parent = TreeNode(1)
parent.left = TreeNode(2)
parent.right = TreeNode(3)
parent.left.left = TreeNode(4)
parent.left.right = TreeNode(5)
parent.right.left = TreeNode(6)
parent.right.right = TreeNode(7)
print(balance(parent))
print(balanceopt(parent))
