from math import inf
from typing import Optional

from Tree.Leetcode.node import TreeNode


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def _validate(root: Optional[TreeNode], min_val: float, max_val: float) -> bool:
            if root is None:
                return True
            if root.val <= min_val or root.val >= max_val:
                return False

            return _validate(root.left, min_val, root.val) and _validate(root.right, root.val, max_val)

        return _validate(root, -float(inf), float(inf))
