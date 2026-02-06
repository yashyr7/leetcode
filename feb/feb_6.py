class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        start = 0
        end = 0
        max_len = -1
        while True:
            
            while end < len(nums) and nums[end] <= nums[start] * k:
                end += 1
            
            max_len = max(max_len, end - start)

            if end == len(nums):
                break

            while start < end and nums[end] > nums[start] * k:
                start += 1

        return len(nums) - max_len