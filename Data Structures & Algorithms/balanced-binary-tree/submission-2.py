# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:


        def get_height_imb(node:TreeNode) -> int:
            if not node:
                return 0

            lefth = get_height_imb(node.left)
            righth = get_height_imb(node.right)

            if (lefth == -1 or righth == -1):
                return -1

            if (abs(lefth-righth) > 1):
                return -1

            return 1+ max(lefth, righth)

        return get_height_imb(root) != -1

        