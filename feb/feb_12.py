class Solution:
    def longestBalanced(self, s: str) -> int:
        ret = -1
        for i in range(len(s)):
            cnt = {}
            for j in range(i, len(s)):
                if s[j] not in cnt:
                    cnt[s[j]] = 1
                else:
                    cnt[s[j]] += 1

                flag = True
                temp = None
                for k in cnt:
                    if temp is None:
                        temp = cnt[k]
                    elif temp != cnt[k]:
                        flag = False
                        break
                
                if flag:
                    ret = max(ret, j - i + 1)
        
        return ret