from typing import Optional

from Tree.Leetcode.node import TreeNode


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        max_height: int = 0

        def max_depth_helper(root: TreeNode, height):
            nonlocal max_height
            if root is None:
                return

            if root.right is None and root.left is None:
                max_height = max(max_height, height)

            max_depth_helper(root.left, height + 1)
            max_depth_helper(root.right, height + 1)

        max_depth_helper(root, 0)

        return max_height
