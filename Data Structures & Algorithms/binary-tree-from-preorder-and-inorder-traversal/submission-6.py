# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])
        stack = [root]
        j = 0

        for value in preorder[1:]:
            node = stack[-1]

            if node.val != inorder[j]:
                # Left subtree is not finished
                node.left = TreeNode(value)
                stack.append(node.left)
            else:
                # Finished node(s); return to an ancestor
                while stack and stack[-1].val == inorder[j]:
                    node = stack.pop()
                    j += 1
                # Attach the new node as a right child
                node.right = TreeNode(value)
                stack.append(node.right)

        return root
