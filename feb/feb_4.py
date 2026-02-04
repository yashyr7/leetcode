class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ret = ""
        i = 0
        while True:
            if i < len(strs[0]):
                pre = strs[0][i]

            for s in strs:
                if i >= len(s) or s[i] != pre:
                    return ret
            ret += pre
            i += 1

        return ret