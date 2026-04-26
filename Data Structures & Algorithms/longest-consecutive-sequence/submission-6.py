class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # identify the start of a sequence
        # if nums[i]-1 is not in the array then it's the beginning of a seq
        numset = set(nums)
        maxcount = 0
        for n in nums:
            if n-1 in numset:
                continue
            # otherwise, this is the start of a sequence
            count = 1
            while n+1 in numset:
                count += 1
                n +=1
            maxcount = max(maxcount, count)
        return maxcount