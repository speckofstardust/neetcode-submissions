class Solution:
    def trap(self, height: List[int]) -> int:
        # Time: O(n)
        # Space: O(n)
        #we need min(max_on_left, max_on_right) - h[i] to know how many units of water can be stored in ith place
        water = 0
        lmax = [0]*len(height)
        for i in range(1, len(height)):
            lmax[i] = max(lmax[i-1], height[i-1])
        
        rmax = minlrmax = [0]*len(height)
        for i in range(len(height)-2, -1, -1):
            rmax[i] = max( rmax[i+1], height[i+1])
            minlrmax[i] = min(lmax[i], rmax[i])

        for i in range(len(height)):
            water += max(0, minlrmax[i] - height[i])

        return water

