class Solution:
    def minPartitions(self, n: str) -> int:
        ret = 0

        for s in n:
            ret = max(int(s), ret)
        
        return ret