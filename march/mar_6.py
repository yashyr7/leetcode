class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        found = False

        for i in range(1, len(s)):
            if s[i - 1] == "1" and s[i] == "0":
                if found == True:
                    return False
                found = True
        
        return False if s[len(s) - 1] == "1" and found == True else True