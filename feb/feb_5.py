class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        res = []
        i = 0
        while i < len(nums):
            j = i
            if nums[i] > 0:
                j = (j + nums[i]) % len(nums)
                res.append(nums[j])
            elif nums[i] < 0:
                j = (j - abs(nums[i])) % len(nums)
                res.append(nums[j])
            else:
                res.append(nums[i])
            i += 1
        
        return res
