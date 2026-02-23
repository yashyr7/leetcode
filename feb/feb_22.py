class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        cnt = 0
        seen = set()

        curr = ""
        end = 0
        while end < len(s) and end < k:
            curr += s[end]
            end += 1

        while end < len(s):
            if curr not in seen:
                cnt += 1
                seen.add(curr)
            
            curr = curr[1:] + s[end]
            end += 1
        
        if curr not in seen:
            cnt += 1
            seen.add(curr)
        
        return cnt == 2**k