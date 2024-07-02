# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        right_depth = self.maxDepth(root.right)
        left_depth = self.maxDepth(root.left)
        
        return max(right_depth, left_depth) + 1

        """
        Solution #2 Iterative (BFS)
    
        if root is None:
                return 0
                
        count = 0
        queue = [root]
        while queue:
            level_len = len(queue)
            for _ in range(level_len):
                node = queue.pop(0)
    
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
            count += 1
        return count
        """
