# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        arr = []

        def dfs(n):
            nonlocal arr
            if n is None:
                return
            
            dfs(n.left)
            arr.append(n.val)
            dfs(n.right)
        
        dfs(root)

        ret = TreeNode()
        
        def buildTree(start, end):
            if start > end:
                return None
            mid = start + (end - start + 1) // 2
            print(mid)
            new = TreeNode(arr[mid])
            new.left = buildTree(start, mid - 1)
            new.right = buildTree(mid + 1, end)

            return new
        
        return buildTree(0, len(arr) - 1)
