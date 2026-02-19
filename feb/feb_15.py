class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a) - 1
        j = len(b) - 1
        ret = ""
        carry = False
        while i >= 0 and j >= 0:
            if a[i] == '1' and b[j] == '1':
                if carry:
                    ret = '1' + ret
                else:
                    ret = '0' + ret
                carry = True

            elif a[i] == '1' or b[j] == '1':
                if carry:
                    ret = '0' + ret
                    carry = True
                else:
                    ret = '1' + ret
                    carry = False
            else:
                if carry:
                    ret = '1' + ret
                else:
                    ret = '0' + ret
                carry = False
            i -= 1
            j -= 1
        
        if i >= 0:
            while i >= 0:
                if a[i] == '1' :
                    if carry:
                        ret = '0' + ret
                        carry = True
                    else:
                        ret = '1' + ret
                        carry = False
                else:
                    if carry:
                        ret = '1' + ret
                    else:
                        ret = '0' + ret
                    carry = False
                i -= 1
        elif j >= 0:
            while j >= 0:
                if b[j] == '1':
                    if carry:
                        ret = '0' + ret
                        carry = True
                    else:
                        ret = '1' + ret
                        carry = False
                else:
                    if carry:
                        ret = '1' + ret
                    else:
                        ret = '0' + ret
                    carry = False
                j -= 1
        
        if carry:
            return '1' + ret
        else:
            return ret
