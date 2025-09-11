from typing import List


class Solution:

    # brute force
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        for i in range(0, len(heights)):
            min_height = heights[i]
            for j in range(i, len(heights)):
                min_height = min(min_height, heights[j])
                curr_area = ((j - i) + 1) * min_height
                max_area = max(curr_area, max_area)
        return max_area