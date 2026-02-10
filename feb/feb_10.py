class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        max_len = 0

        for i in range(len(nums)):
            even = 0
            odd = 0
            seen = set()
            for j in range(i, len(nums)):
                if nums[j] not in seen and nums[j] % 2 == 1:
                    odd += 1
                elif nums[j] not in seen and nums[j] % 2 == 0:
                    even += 1
                
                seen.add(nums[j])

                if even == odd:
                    max_len = max(j - i + 1, max_len)
        
        return max_len
