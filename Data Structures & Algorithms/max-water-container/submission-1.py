class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_container = 0

        while l < r:
            area = (r - l) * min(heights[l], heights[r])
            max_container = max(max_container, area)

            if heights[l] <= heights[r]:
                l += 1
            elif heights[r] < heights[l]:
                r -= 1

        return max_container 
        