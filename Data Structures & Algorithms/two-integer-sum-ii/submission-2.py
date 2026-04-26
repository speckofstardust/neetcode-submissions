class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #since numbers is sorted, target = smaller_num + bigger_num
        # if the sum < target, increase teh smaller number
        #  if sum > target, decrease the bigger number
        i, j = 0, len(numbers)-1
        while i<j:
            if numbers[i] + numbers[j] == target:
                return [i+1,j+1]
            elif numbers[i] + numbers[j] < target:
                i += 1
            else:
                j -= 1
        
        