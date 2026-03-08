class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        nums = set(nums)
        ret = ""

        def generate(curr):
            nonlocal ret
            if len(curr) == n:
                if curr not in nums:
                    ret = curr
                return
            
            generate(curr + "0")
            generate(curr + "1")
        
        generate("")
        return ret

            
