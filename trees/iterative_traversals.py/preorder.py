class TreeNode:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val
def pre(parent):
    if parent is None:
        return []
    stack=[parent]
    result=[]
    while stack:
        curr=stack.pop()
        result.append(curr.val)
        if curr.right:
            stack.append(curr.right)
        if curr.left:
            stack.append(curr.left)
    return result
parent = TreeNode(1)
parent.left = TreeNode(2)
parent.right = TreeNode(3)
parent.left.left = TreeNode(4)
parent.left.right = TreeNode(5)
parent.right.left = TreeNode(6)
parent.right.right = TreeNode(7)
print(pre(parent))
