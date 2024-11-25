class TreeNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

def zigzag(root):
    result=[]
    q=[root]
    ltr=True
    while q:
        temp=[]
        for i in range(len(q)):
            cur=q.pop(0)
            if ltr:
                temp.append(cur.val)
            else:
                temp.insert(0,cur.val)
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
        ltr=not ltr
        result.extend(temp)
    return result

           
           
parent = TreeNode(1)
parent.left = TreeNode(2)
parent.right = TreeNode(3)
parent.left.left = TreeNode(4)
parent.left.right = TreeNode(5)
# parent.right.left = TreeNode(6)
parent.right.right = TreeNode(6)

print(zigzag(parent))
