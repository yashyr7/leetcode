class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        prev = ["0"]
        cnt = 1

        while cnt <= n:
            new = []

            for ch in prev:
                new.append(ch)
            
            new.append("1")

            for i in range(len(prev) - 1, -1, -1):
                if prev[i] == "1":
                    new.append("0")
                else:
                    new.append("1")
            
            cnt += 1
            prev = new
        
        return prev[k - 1]


