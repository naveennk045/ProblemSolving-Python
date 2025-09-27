from typing import Optional, List


# Definition for a Node.

class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: 'Node') -> List[int]:

        traversal_ans = []

        def postorder_utils(node: 'Node'):
            if not node:
                return

            for child in node.children:
                postorder_utils(child)

            # print(node.val)
            traversal_ans.append(node.val)

        postorder_utils(root)
        return traversal_ans