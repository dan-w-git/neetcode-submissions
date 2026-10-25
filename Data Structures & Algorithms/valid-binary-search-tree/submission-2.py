# DS: Tree
# ALGO: DFS
# Time: O(n^2). Space: O(h)
# Time O(n²) worst case for a skewed tree, and O(n log n) for a balanced one
# Space: at any moment the stack holds at most: d (isValidBST frames) + (h - d) (helper frames) ≈ h

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def isValid(node, low, high):
            if not node:
                return True

            if not (low < node.val < high):
                return False
            
            return isValid(node.left, low, node.val) and isValid(node.right, node.val, high)

        return isValid(root, float("-inf"), float("inf"))

