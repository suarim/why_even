from collections import defaultdict
class TreeNode:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val
def bottom(root):
    d={}
    def trav(root,key,lvl):
        if not root:
            return 
        if key not in d:

            d[key]=([root.val,lvl])
            print(d)
        else:
            if lvl>d[key][1]:
                d[key]=[root.val,lvl]
        trav(root.left,key-1,lvl+1)
        trav(root.right,key+1,lvl+1)
    trav(root,0,0)
    return [d[k][0] for k in sorted(d)]
parent = TreeNode(1)
parent.left = TreeNode(2)
parent.right = TreeNode(3)
parent.left.right = TreeNode(4)
parent.left.right.left = TreeNode(6)
parent.left.right.left.left = TreeNode(8)
parent.right.right = TreeNode(5)
parent.right.right.left = TreeNode(7)
print(bottom(parent))
