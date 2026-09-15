# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        self.pIdx = 0
        # for (idx,val) pair in inorder list, create map with pair (val, idx) for O(1) lookup
        in_map = {val:idx for idx,val in enumerate(inorder)}

        def dfs(left, right):
            if left > right:
                return None

            # current root of tree/subtree is first appearing item in preorder list as we increment
            root_val = preorder[self.pIdx]
            self.pIdx += 1

            # index of root_val in inorder list
            idx = in_map[root_val]
            # create a new node for current root of tree/subtree
            root = TreeNode(root_val)

            root.left = dfs(left, idx-1)
            root.right = dfs(idx+1, right)

            return root

        return dfs(0, len(inorder)-1)


