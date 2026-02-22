class Solution:
    def binaryGap(self, n: int) -> int:
        ret = 0
        cnt = 0

        while n > 0:
            if n % 2:
                n = n // 2
                break
            n = n // 2
        
        while n > 0:
            cnt += 1
            
            if n % 2:
                ret = max(ret, cnt)
                cnt = 0
            
            n = n // 2

        return ret