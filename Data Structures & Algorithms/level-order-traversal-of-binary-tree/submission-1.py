# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # level order traverl -> BFS
        if not root:
            return []

        queue = deque()
        queue.append(root)
        res = []
        
        while queue:
            level_size = len(queue)
            level = []
            for _ in range(level_size): 
                # add curr node to list
                curr = queue.popleft()
                level.append(curr.val)
                # add curr's left val
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

            res.append(level)

        return res
