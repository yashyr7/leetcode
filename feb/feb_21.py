class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        ret = 0
        s = {2,3,5,7,11,13,17,19}
        for i in range(left, right + 1):
            n = i
            cnt = 0
            while n > 0:
                if n % 2:
                    cnt += 1
                n = n // 2
            
            if cnt in s:
                ret += 1
        
        return ret