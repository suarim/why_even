from collections import deque
class TreeNode:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val
def maxwidth(root):
    
    if not root:
        return 0
    res=0
    prevlvl,prevnum=0,0
    q=deque([[root,1,0]])
    while q:
        node,num,lvl=q.popleft()
        if lvl>prevlvl:
            prevlvl,prevnum=lvl,num
        res=max(res,num-prevnum+1)
        if node.left:
            q.append([node.left,2*num,lvl+1])
        if node.right:
            q.append([node.right,2*num+1,lvl+1])
    return res
parent = TreeNode(1)
parent.left = TreeNode(2)
parent.right = TreeNode(3)
parent.left.left = TreeNode(4)
parent.left.right = TreeNode(5)
parent.right.left = TreeNode(6)
parent.right.right = TreeNode(7)
parent.left.left.left = TreeNode(8)
parent.right.right.right = TreeNode(9)
print(maxwidth(parent))