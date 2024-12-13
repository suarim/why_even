from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def burn(gb, root: TreeNode):
    parents = {}

    # Build the parent mapping for the entire tree
    def build_parents(node, parent=None):
        if not node:
            return
        if parent:
            parents[node] = parent
        build_parents(node.left, node)
        build_parents(node.right, node)

    build_parents(gb)
    for i,j in parents.items():
        print(i.val,j.val)
    q=deque([(root,0)])
    visited=set()
    res=0
    while q:
        cur,time=q.popleft()
        res=max(res,time)
        if cur in visited:
            continue
        visited.add(cur)
        # print(cur.val)
        # for i in visited:
        #     print("in visited->",i.val)
        # res+=1
        if cur.left and cur.left not in visited:
            q.append((cur.left,time+1))
        if cur.right and cur.right not in visited:
            q.append((cur.right,time+1))
        if cur in parents and parents[cur] not in visited:
            q.append((parents[cur],time+1))
        # for i in q:
        #     print(i[0].val,i[1])
    return res

# Construct the binary tree
parent = TreeNode(1)
parent.left = TreeNode(2)
parent.right = TreeNode(3)
parent.left.left = TreeNode(4)
parent.left.right = TreeNode(5)
parent.right.right = TreeNode(6)
parent.left.right.left = TreeNode(7)
parent.left.right.right = TreeNode(8)
parent.right.right.right=TreeNode(9)
parent.right.right.right.right=TreeNode(10)



# Call the function and print the output
print(burn(parent, parent.left.right.right))
