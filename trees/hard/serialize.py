class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def serialize(root):
    res=[]
    q=[root]
    while q:
        cur=q.pop(0)
        if cur:
            res.append(cur.val)
            q.append(cur.left)
            q.append(cur.right)
        else:
            res.append('null')
    return res
def deserialize(data):
    if not data:
        return None
    root=TreeNode(data[0])
    q=[root]
    i=1
    while i<len(data):
        cur=q.pop(0)
        if data[i]!='null':
            cur.left=TreeNode(data[i])
            q.append(cur.left)
        i+=1
        if data[i]!='null' and i<len(data):
            cur.right=TreeNode(data[i])
            q.append(cur.right)
        i+=1
    return root
def printtrees(root):
    if not root:
        return 
    printtrees(root.left)
    print(root.val)
    printtrees(root.right)
    return
parent = TreeNode(1)
parent.left = TreeNode(2)
parent.right = TreeNode(3)
parent.left.left = TreeNode(4)
parent.left.right = TreeNode(5)
parent.right.right = TreeNode(6)
parent.left.right.left = TreeNode(7)
# parent.left.right.right = TreeNode(8)
# parent.right.right.right=TreeNode(9)
# parent.right.right.right.right=TreeNode(10)
x=serialize(parent)
print(serialize(parent)) 
y=deserialize(x)
print(printtrees(deserialize(x)))
print(serialize(deserialize(x)))