preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
def buildTree(preorder, inorder) :
    inmap={}
    for i,n in enumerate(inorder):
        inmap[n]=i
    def xbuilder(inmap,prestart,preend,instart,inend,inorder,preorder):
        if prestart>preend or instart>inend:
            return None
        root=TreeNode(preorder[prestart])
        inroot=inmap[root.val]
        numsleft=inroot-instart
        root.left=xbuilder(inmap,prestart+1,prestart+numsleft,instart,inroot-1,inorder,preorder)
        root.right=xbuilder(inmap,prestart+numsleft+1,preend,inroot+1,inend,inorder,preorder)
        return root
    root=xbuilder(inmap,0,len(preorder)-1,0,len(inorder)-1,inorder,preorder)
    return root
def printTree(root):
    if root:
        print(root.val)
        printTree(root.left)
        printTree(root.right)
print(printTree(buildTree(preorder,inorder)))