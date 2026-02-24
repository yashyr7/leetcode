# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        ret = 0

        def dfs(n, b):
            nonlocal ret
            if n.left is None and n.right is None:
                ret += int(b + str(n.val), 2)
                return
            if n.left:
                dfs(n.left, b + str(n.val))
            if n.right:
                dfs(n.right, b + str(n.val))

        dfs(root, "")
        return ret
