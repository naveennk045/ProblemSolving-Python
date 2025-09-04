from collections import deque
from typing import Optional, List

from Tree.Leetcode.node import TreeNode


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        result = [[]]
        is_reverse = False
        queue.append(root)

        while queue:

            level_size = len(queue)
            curr_level = []

            for i in range(0, level_size):
                curr_root = queue.popleft()
                curr_level.append(curr_root.val)

                if curr_root.left:
                    queue.append(curr_root.left)
                if curr_root.right:
                    queue.append(curr_root.right)

            if is_reverse:
                curr_level.reverse()

            result.append(curr_level)
            is_reverse = not is_reverse
        return result