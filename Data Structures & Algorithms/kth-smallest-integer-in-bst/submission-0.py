# DS: BST
# ALGO: DFS
# Time: O(h + k). Space: O(h)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:      
        result = root.val
        counter = k

        # in-order traversal: visits BST in sorted order (guaranteed)
        def dfs(node):
            nonlocal result, counter

            if not node:
                return            

            dfs(node.left)

            if counter == 0:    # check counter before updating result
                return

            result = node.val
            counter -= 1

            if counter == 0:    # check counter before calling dfs on right subtree
                return

            dfs(node.right)

        dfs(root)
        return result
