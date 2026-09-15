# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        # traverse through the root
        # if same node as subroot is found, start check

        # helper function to determine if the two trees are the same staring at the same root 
        def helper(node, subNode):
            if not node and not subNode:
                return True
            if node and subNode and node.val == subNode.val:
                return helper(node.left, subNode.left) and helper(node.right, subNode.right)
            else:
                return False


        if not subRoot:
            return True
        if not root:
            return False
        if helper(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

       
