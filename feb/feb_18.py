class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        b = bin(n)
        start = 2
        if n < 0:
            start = 3
        
        prev = None
        for i in range(start, len(b)):
            if prev is None:
                prev = b[i]
            elif prev == b[i]:
                return False
            else:
                prev = b[i]
        
        return True
