from typing import Optional

from Tree.Leetcode.node import TreeNode


class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return False

        if not root.left and not root.right:
            return False if root.val == 0 else True

        left = self.evaluateTree(root.left)
        right = self.evaluateTree(root.right)

        if root.val == 2:
            return left or right

        return left and right
