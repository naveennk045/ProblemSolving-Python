from typing import Optional

from Tree.Leetcode.node import TreeNode


class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        max_abs_val = 0

        def _helper(root: Optional[TreeNode], depth: int, ancestor: Optional[TreeNode]):
            global max_abs_val
            if root is None:
                return
            if depth > 3:
                return
            max_abs_val  = max(abs(ancestor.val - root.val), max_abs_val)

            _helper(root.left, depth + 1, ancestor)
            _helper(root.right, depth + 1, ancestor)

            _helper(root.left, depth + 1, root)
            _helper(root.right, depth + 1, root)
        _helper(root,0,root)

        return max_abs_val