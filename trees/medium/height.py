class TreeNode:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val
def maxh(root):
    if root is None:
        return 0
    return 1+max(maxh(root.left),maxh(root.right))
def maxhbfs(root):
    if root is None:
        return 0
    q=[root]
    c=0
    while q:
        n=len(q)
        for _ in range(n):
            node=q.pop(0)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        c+=1
    return c
parent = TreeNode(1)
parent.left = TreeNode(2)
parent.right = TreeNode(3)
parent.left.left = TreeNode(4)
parent.left.right = TreeNode(5)
parent.right.left = TreeNode(6)
parent.right.right = TreeNode(7)
print(maxh(parent))
print(maxhbfs(parent))
