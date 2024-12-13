postorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
def buildTree(inorder, postorder) :
        inmap={}
        for i,n in enumerate(inorder):
            inmap[n]=i
        def xbuilder(ps,pe,inmap,ise,ie,inorder,postorder):
            if ps>pe or ise>ie:
                return None
            root=TreeNode(postorder[pe])
            inroot=inmap[postorder[pe]]
            numsleft=inroot-ise
            root.left=xbuilder(ps,ps+numsleft-1,inmap,ise,inroot-1,inorder,postorder)
            root.right=xbuilder(ps+numsleft,pe-1,inmap,inroot+1,ie,inorder,postorder)
            return root
        root=xbuilder(0,len(postorder)-1,inmap,0,len(inorder)-1,inorder,postorder)
        return root
def printTree(root):
    if root:
        print(root.val)
        printTree(root.left)
        printTree(root.right)
print(printTree(buildTree(postorder,inorder)))