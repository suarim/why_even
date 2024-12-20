from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def distanceK(gb,root: TreeNode, k: int):
    parents = {}
    
    
    def build_parents(node, parent=None):
        if not node:
            return
        if parent:
            parents[node] = parent
        build_parents(node.left, node)
        build_parents(node.right, node)
    build_parents(gb)
    
    visited = set()
    results=[]
    q = deque([(root, 0)])
    while q:
        cur,dist=q.popleft()
        if cur in visited:
            continue
        if dist==k:
            results.append(cur.val)
        visited.add(cur)
        if cur.left and cur.left not in visited:
            q.append((cur.left, dist+1))
        if cur.right and cur.right not in visited:
            q.append((cur.right, dist+1))
        if cur in parents and parents[cur] not in visited:
            q.append((parents[cur], dist+1))
    return results

# Construct the binary tree
parent = TreeNode(1)
parent.left = TreeNode(2)
parent.right = TreeNode(3)
parent.left.left = TreeNode(4)
parent.left.right = TreeNode(5)
parent.right.left = TreeNode(6)
parent.right.right = TreeNode(7)

# Call the function and print the output
print(distanceK(parent,parent.left, 2))
