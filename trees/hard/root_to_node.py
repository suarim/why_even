class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
def root_to_node(root, node):
    arr=[]
    if not root:
        return []
    def trav(root,node):
        if not root:
            return False
        arr.append(root.value)
        if root.value==node:
            return True
        if trav(root.left,node) or trav(root.right,node):
            return True
        arr.pop()
        return False
    trav(root,node)
    return arr


parent = TreeNode(1)
parent.left = TreeNode(2)
parent.right = TreeNode(3)
parent.left.left = TreeNode(4)
parent.left.right = TreeNode(5)
parent.right.left = TreeNode(6)
parent.right.right = TreeNode(7)
print(root_to_node(parent, 7)) # [1, 2, 5]