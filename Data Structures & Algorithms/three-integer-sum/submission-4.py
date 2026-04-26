class Solution:
    def threeSum(self, nums: List[int]) -> List[int]:
        #if I sort nums, I can just skip if I've checked for that number already to eal with the duplicates
        #target = -nums[i], 2Sum on the rest of the array for the target
        nums = sorted(nums) #O(nlog(n))
        res = []
        for i in range(len(nums)):
            if i != 0 and nums[i] == nums[i-1]: #to ensure no duplicate 1st value
                continue
            j = i + 1
            k = len(nums) - 1
            target = -nums[i]
            while j<k:
                if target == nums[j] + nums[k]:
                    res.append([nums[i], nums[j], nums[k]])
                    while j<k and nums[j] == nums[j+1]: #to skip duplicate 2nd value
                        j += 1
                    while j<k and nums[k] == nums[k-1]: #to skip duplicate 3rd value
                        k -= 1
                    j += 1
                    k -= 1
                elif target > nums[j] + nums[k]:
                    j += 1
                else:
                    k -= 1
        return res
