from typing import Optional

from Tree.Leetcode.node import TreeNode


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if root is None:
            return None

        temp_node = root.left

        root.left = self.invertTree(root.right)
        root.right = self.invertTree(temp_node)

        return root
