class TreeNode:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val
def left(root):
    result=[]
    if root is None:
        return []
    if root.left is not None:
        result.append(root.val)
        result+=left(root.left)
    elif root.left is None and root.right is not None:
        result.append(root.val)
        result+=left(root.right)
    return result
def right(root):
    result=[]
    if root is None:
        return []
    if root.right is not None:
        result+=right(root.right)
        result.append(root.val)
    elif root.right is None and root.left is not None:
        result+=right(root.left)
        result.append(root.val)
    return result
def leaf(root):
    result=[]
    if root is None:
        return []
    if root.left is None and root.right is None:
        result.append(root.val)
    result.extend(leaf(root.left))
    result.extend(leaf(root.right))
    return result
parent = TreeNode(1)
parent.left = TreeNode(2)
parent.right = TreeNode(3)
parent.left.left = TreeNode(4)
parent.left.right = TreeNode(5)
parent.right.left = TreeNode(6)
parent.right.right = TreeNode(7)
x=left(parent)
z=right(parent)[:-1][::-1]
y=leaf(parent)
print(x+y+z)