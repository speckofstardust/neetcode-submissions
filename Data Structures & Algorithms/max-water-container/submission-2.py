class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #farther the value of i and j, the better
        i, j = 0, len(heights)-1
        res = 0
        while i < j:
            area = (j-i)*min(heights[i],heights[j])
            res = max(res, area)
            #updating pointer logic
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return res