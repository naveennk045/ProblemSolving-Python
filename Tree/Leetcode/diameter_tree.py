from typing import Optional

from Tree.Leetcode.node import TreeNode


# Optimal approach
class Solution1:
    max_height = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        Solution1.max_height = 0
        Solution1.diameter_helper(root)
        return Solution1.max_height

    @staticmethod
    def diameter_helper(root: TreeNode):
        if root is None:
            return 0

        left_height = Solution1.diameter_helper(root.left)
        right_height = Solution1.diameter_helper(root.right)

        Solution1.max_height = max(Solution1.max_height, left_height + right_height)

        return max(left_height, right_height) + 1


# Brute force approach
class Solution2:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_height = 0

        def helper(node) -> None:
            nonlocal max_height
            if node is None:
                return

            max_height = max(
                Solution2.find_height_of_tree(node.left) + Solution2.find_height_of_tree(node.right)
                , max_height)

            helper(node.left)
            helper(node.right)

        helper(root)
        return max_height

    @staticmethod
    def find_height_of_tree(root: Optional[TreeNode]):

        if root is None:
            return 0
        return max(Solution2.find_height_of_tree(root.left), Solution2.find_height_of_tree(root.right)) + 1
