class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        first = float('inf')
        second = float('inf')
        
        for n in nums[1:]:
            if n <= first:
                second = first
                first = n
            elif n <= second:
                second = n
            
        return nums[0] + first + second
    