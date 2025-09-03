from typing import Optional

from Tree.Leetcode.Node import TreeNode


class Solution:

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return Solution.is_symmetric_helper(root,root)

    @staticmethod
    def is_symmetric_helper(node1 : TreeNode , node2 : TreeNode) -> bool:

        if node1 is None and node2 is None:
            return True
        if node1 is None or node2 is None:
            return False

        if node1.val != node2.val:
            return False

        return Solution.is_symmetric_helper(node1.left,node2.right) and Solution.is_symmetric_helper(node1.right,node2.left)



