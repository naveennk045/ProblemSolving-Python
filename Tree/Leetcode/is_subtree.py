from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def is_same(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

            if not root1 and not root2:
                return True
            if not root1 or not root2:
                return False
            if root1.val != root2.val:
                return False

            return is_same(root1.left, root2.left) and is_same(root1.right, root2.right)

        def is_subtree_helper(root: 'TreeNode', sub_root: 'TreeNode') -> bool:

            if not root and not root:
                return False
            if not root or not sub_root:
                return False
            if root.val == sub_root.val:
                if is_same(root, sub_root):
                    return True
            return is_subtree_helper(root.left, sub_root) or is_subtree_helper(root.right, sub_root)

        return is_subtree_helper(root, subRoot)
