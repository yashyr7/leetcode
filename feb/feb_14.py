class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [[0] * k for k in range(1, 102)]

        dp[0][0] = poured

        for r in range(query_row + 1):
            for c in range(r + 1):
                q = (dp[r][c] - 1) / 2
                if q > 0:
                    dp[r + 1][c] += q
                    dp[r + 1][c + 1] += q
        
        return min(dp[query_row][query_glass], 1)

            
