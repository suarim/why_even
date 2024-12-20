class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def buildTree(inorder, postorder):
    if not inorder or not postorder:
        return None
    root_val=postorder.pop()
    root=TreeNode(root_val)
    root_index=inorder.index(root_val)
    root.right=buildTree(inorder[root_index+1:],postorder)
    root.left=buildTree(inorder[:root_index],postorder)
    return root


def printTree(root):
    if root:
        print(root.val)
        printTree(root.left)
        printTree(root.right)

# Example usage
postorder =[9, 15, 7, 20, 3]
inorder = [9, 3, 15, 20, 7]
root = buildTree(inorder, postorder)
printTree(root)
