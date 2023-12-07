# Definition for a binary tree node to sol
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sortedArrayToBST(nums):
    if not nums:
        return None

    mid = len(nums) // 2

    root = TreeNode(nums[mid])
    root.left = sortedArrayToBST(nums[:mid])
    root.right = sortedArrayToBST(nums[mid + 1:])

    return root

def printTree(root):
    def getHeight(node):
        if not node:
            return 0
        return 1 + max(getHeight(node.left), getHeight(node.right))

    def printNodes(node, level, pos):
        if not node:
            return
        if level == 1:
            nodes[pos] = str(node.val).center(width)
        else:
            gap = " " * width
            printNodes(node.left, level - 1, pos - 2 ** (level - 2))
            printNodes(node.right, level - 1, pos + 2 ** (level - 2))

    height = getHeight(root)
    width = 3 * 2 ** (height - 1)

    nodes = [""] * width
    for i in range(1, height + 1):
        printNodes(root, i, 2 ** (height - i) - 1)
        print("".join(nodes))
        nodes = [""] * width

# Example usage
nums1 = [-10, -3, 0, 5, 9]
result1 = sortedArrayToBST(nums1)
print("Example 1:")
printTree(result1)

nums2 = [1, 3]
result2 = sortedArrayToBST(nums2)
print("\nExample 2:")
printTree(result2)

