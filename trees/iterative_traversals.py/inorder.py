class TreeNode:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val
def inorder(root):
    st=[]
    result=[]
    current=root
    while current or st:
        while current:
            st.append(current)
            current=current.left
        current=st.pop()
        result.append(current.val)
        current=current.right
    return result
parent = TreeNode(1)
parent.left = TreeNode(2)
parent.right = TreeNode(3)
parent.left.left = TreeNode(4)
parent.left.right = TreeNode(5)
parent.right.left = TreeNode(6)
parent.right.right = TreeNode(7)
print(inorder(parent))
