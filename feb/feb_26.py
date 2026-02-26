class Solution:
    def numSteps(self, s: str) -> int:
        ret = 0
        
        while len(s) > 1:
            if s[len(s) - 1] == '1':
                new = "0"
                i = len(s) - 2
                carry = True
                while i >= 0:
                    if carry:
                        if s[i] == '1':
                            new = '0' + new
                        else:
                            new = '1' + new
                            carry = False
                    else:
                        new = s[i] + new
                    i -= 1
                if carry:
                    new = '1' + new
                s = new
            else:
                s = s[:-1]
            ret += 1
        
        return ret
