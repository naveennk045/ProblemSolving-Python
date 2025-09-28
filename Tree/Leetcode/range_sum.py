from typing import Optional

from Tree.Leetcode.node import TreeNode


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

            if not root:
                return 0
            if low <= root.val <= high:
                return root.val

            return self.rangeSumBST(root.left,low,high) + self.rangeSumBST(root.right,low,high)
