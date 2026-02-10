class Solution:
    def minimumDeletions(self, s: str) -> int:
        ret = float('inf')
        a = 0
        b = 0
        before_b = [0 for i in range(len(s))]
        after_a = [0 for i in range(len(s))]
        
        for i in range(len(s)):
            before_b[i] = b
            if s[i] == 'b':
                b += 1
        
        for i in range(len(s) - 1, -1, -1):
            after_a[i] = a
            if s[i] == 'a':
                a += 1
        
        for i in range(len(s)):
            ret = min(ret, before_b[i] + after_a[i])
        
        return ret


