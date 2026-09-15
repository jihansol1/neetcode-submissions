# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # BST: left subtree is all less than node, right subtree is al greater than node
        # if node is greater than p and q, they are in left side
        # if node is less than p and q, they are in right side
        # if node is greater than one but less than the other, it is the lca (split point)

        if not root or not p or not q:
            return None

        if q.val < root.val and p.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif q.val > root.val and p.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
            