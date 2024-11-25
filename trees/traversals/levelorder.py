class TreeNode:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val
def level(root):
    if root is None:
        return []
    q=[root]
    result=[]
    while q:
        curr=q.pop(0)
        result.append(curr.val)
        if curr.left:
            q.append(curr.left)
        if curr.right:
            q.append(curr.right)
        
    return result
parent = TreeNode(1)
parent.left = TreeNode(2)
parent.right = TreeNode(3)
parent.left.left = TreeNode(4)
parent.left.right = TreeNode(5)
parent.right.left = TreeNode(6)
parent.right.right = TreeNode(7)
print(level(parent))
