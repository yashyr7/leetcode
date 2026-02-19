class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        ret = 0
        prev = 0
        curr = 1
        for i in range(1, len(s)):
            if s[i] != s[i - 1]:
                ret += min(prev, curr)
                prev = curr
                curr = 1
            else:
                curr += 1
        
        ret += min(prev, curr)
        
        return ret
