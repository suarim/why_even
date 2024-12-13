

class TreeNode:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val

def trav(root):
    result=[]
    if not root:
        return []
    result.extend(trav(root.left))
    result.append(root.val)
    result.extend(trav(root.right))
    return result
parent = TreeNode(1)
parent.left = TreeNode(2)
parent.right = TreeNode(3)
parent.left.left = TreeNode(4)
parent.left.right = TreeNode(5)
parent.right.left = TreeNode(6)
parent.right.right = TreeNode(7)
result=trav(parent)
print(result)
print(len(result))        