class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        d = []

        for n in arr:
            b = bin(n)[2:]
            cnt = 0
            for ch in b:
                if ch == '1':
                    cnt += 1
            
            d.append([b, cnt])
        
        d.sort(key= lambda x: (x[1], int(x[0], 2)))

        ret = []

        for i in d:
            ret.append(int(i[0], 2))
        
        return ret