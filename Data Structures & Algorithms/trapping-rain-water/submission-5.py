class Solution:
    def trap(self, height: List[int]) -> int:
        # Time: O(n)
        # Space: O(1)
        #we need min(max_on_left, max_on_right) - h[i] to know how many units of water can be stored in ith place
        l, r = 0, len(height) - 1
        lmax, rmax = height[l], height[r]
        water = 0
        i = 0
        while l < r:          
            #pointer updation logic
            #move the pointer for whichever is lesser among maxl, minl
            #update l, r, i
            if rmax < lmax:
                r -= 1
                rmax = max(rmax, height[r])
                water += max(0, rmax - height[r])
            else:
                l += 1
                lmax = max(lmax, height[l])
                water += max(0, lmax - height[l])

        return water

