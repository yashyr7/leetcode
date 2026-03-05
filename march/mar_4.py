class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        r = [0] * len(mat)
        c = [0] * len(mat[0])

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    r[i] += 1
                    c[j] += 1
        
        cnt = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1 and r[i] == 1 and c[j] == 1:
                    cnt += 1
        
        return cnt