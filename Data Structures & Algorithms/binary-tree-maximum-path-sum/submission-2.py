# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]
        def dfs(node):
            if not node:
                return 0
            leftNode = dfs(node.left)
            rightNode = dfs(node.right)
            maxLeft = max(0, leftNode)
            maxRight = max(0, rightNode)
            res[0] = max(res[0], node.val + maxLeft + maxRight)
            return node.val + max(maxLeft, maxRight)
        dfs(root)
        return res[0]