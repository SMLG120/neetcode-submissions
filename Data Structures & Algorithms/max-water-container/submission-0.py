class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # brute force approach
        res = 0
        for l in range(len(heights)):
            for r in range(1, len(heights)):
                minHeight = min(heights[l], heights[r])
                area = (r - l) * minHeight
                res = max(res, area)
        return res

