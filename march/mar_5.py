class Solution:
    def minOperations(self, s: str) -> int:
        a = 0
        b = 0
        c = "1"
        d = "0"

        for ch in s:
            if ch != c:
                a += 1
            if ch != d:
                b += 1

            c = "1" if c == "0" else "0"
            d = "1" if d == "0" else "0"

        return min(a, b)