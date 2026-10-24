# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        sublist = []
        queue = deque()

        if not root:
            return result

        queue.append((root, 0))   # (node, lvl)
        current_lvl = 0
        
        while queue:
            node, lvl = queue[0]

            if not node:
                queue.popleft()
                continue

            if lvl > current_lvl:
                result.append(sublist)
                sublist = []
                current_lvl += 1
            
            sublist.append(node.val)
            queue.popleft()
            queue.append((node.left, lvl+1))
            queue.append((node.right, lvl+1))
            
        result.append(sublist)
        return result
