class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def lowestCommonAncestor(root, p, q):
    if not root:
        return None
    
    if root.val > p.val and root.val > q.val:
        return lowestCommonAncestor(root.left, p, q)
    elif root.val < p.val and root.val < q.val:
        return lowestCommonAncestor(root.right, p, q)
    else:
        return root

# Test cases
# Constructing the tree from the given input
root = TreeNode(6)
root.left = TreeNode(2)
root.right = TreeNode(8)
root.left.left = TreeNode(0)
root.left.right = TreeNode(4)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)
root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(5)

# Example 1
p1 = TreeNode(2)
q1 = TreeNode(8)
result1 = lowestCommonAncestor(root, p1, q1)
print("Example 1 - LCA of nodes 2 and 8 is:", result1.val)

# Example 2
p2 = TreeNode(2)
q2 = TreeNode(4)
result2 = lowestCommonAncestor(root, p2, q2)
print("Example 2 - LCA of nodes 2 and 4 is:", result2.val)
