class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
def flatten(root):
    if not root:
        return None
    st=[root]
    while st:
        cur=st.pop()
        if cur.right:
            st.append(cur.right)
        if cur.left:
            st.append(cur.left)
        if st:
            cur.right=st[-1]
        cur.left=None
    return root
def printtrees(root):
    if not root:
        return 
    
    print(root.val)
    printtrees(root.right)
    return
parent=TreeNode(1)
parent.left=TreeNode(2)
parent.right=TreeNode(5)
parent.left.left=TreeNode(3)
parent.left.right=TreeNode(4)
parent.right.right=TreeNode(6)
parent.right.right.left=TreeNode(7)
printtrees(flatten(parent))