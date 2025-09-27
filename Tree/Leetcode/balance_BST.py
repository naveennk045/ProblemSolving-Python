from typing import Optional

from Tree.Leetcode.node import TreeNode


class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def calculate_height(root: Optional[TreeNode]):
            if root is None:
                return 0

            left_height = calculate_height(root.left)
            right_height = calculate_height(root.right)

            return max(left_height, right_height) + 1

        def balance_factor(root: Optional[TreeNode]):
            if root is None:
                return 0

            left_height = calculate_height(root)
            right_height = calculate_height(root)

            return left_height - right_height


        def left_rotate(x: Optional[TreeNode]):
            y = x.right
            t2 = y.left

            y.left = x
            x.right = t2

            return y

        def right_rotate(x: Optional[TreeNode]):
            y = x.left
            t2 = y.right

            y.right = x
            x.left = t2

            return y


        def rotate(root: Optional[TreeNode]):

            if root is None:
                return None

            balance_fac = balance_factor(root)
            
            ## left heavy
            if balance_fac > 1 :
                if calculate_height(root.left) > calculate_height(root.right):
                    return right_rotate(root)
                else :
                    root = left_rotate(root)
                    return right_rotate(root)

            ## right heavy
            elif balance_fac < -1 :
                if calculate_height(root.left) < calculate_height(root.right):
                    return left_rotate(root)
                else:
                    root = right_rotate(root)
                    return left_rotate(root)
            return root

        def balance_it(root: Optional[TreeNode]):

            if root is None:
                return None

            balance_it(root.left)
            balance_it(root.right)

        return rotate(root)
