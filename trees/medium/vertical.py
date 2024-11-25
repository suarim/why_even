from collections import defaultdict
class TreeNode:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val
def vertical(root):
    d=defaultdict(list)
    def trav(root,key):
        if not root:
            return 
        d[key].append(root.val)
        trav(root.left,key-1)
        trav(root.right,key+1)
    trav(root,0)
    return [d[k] for k in sorted(d)]
parent = TreeNode(1)
parent.left = TreeNode(2)
parent.right = TreeNode(3)
parent.left.left = TreeNode(4)
parent.left.right = TreeNode(5)
parent.right.left = TreeNode(6)
parent.right.right = TreeNode(7)
print(vertical(parent))
