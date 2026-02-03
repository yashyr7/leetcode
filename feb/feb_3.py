class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        i = 1

        if len(nums) <= 3:
            return False

        cnt = 0

        while i < len(nums):
            if nums[i - 1] == nums[i]:
                return False
            if nums[i - 1] > nums[i]:
                break
            i += 1
            cnt += 1
        
        if i == len(nums) or cnt == 0:
            return False

        cnt = 0

        while i < len(nums):
            if nums[i - 1] == nums[i]:
                return False
            if nums[i - 1] < nums[i]:
                break
            i += 1
            cnt += 1
        
        if i == len(nums) or cnt == 0:
            return False

        while i < len(nums):
            if nums[i - 1] == nums[i]:
                return False
            if nums[i - 1] > nums[i]:
                break
            i += 1
        
        return i == len(nums)