from collections import deque
class TreeNode:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val
def inorder(head):
    results=[]
    if head is None:
        return results
    results.extend(inorder(head.left))
    results.append(head.val)
    results.extend(inorder(head.right))
    return results
def levelorder(head):
    # head
    q=deque([head])
    while q:
        cur=q.popleft()
   
        print(cur.val," ")
        if cur.left:
            q.append(cur.left)
        if cur.right:
            q.append(cur.right)
def height(root):
    if not root:
        return 0
    return max(height(root.left),height(root.right))+1
parent = TreeNode(1)
parent.left = TreeNode(2)
parent.right = TreeNode(3)
parent.left.left = TreeNode(4)
parent.left.right = TreeNode(5)
parent.right.left = TreeNode(7)
parent.right.right = TreeNode(6)
# print(levelorder(parent))
print(height(parent))