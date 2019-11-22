from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [([0] * (amount+1)) for _ in range(len(coins)+1)]
        dp[0][0] = 1
        for i in range(1, len(coins)+1):
            for j, y in enumerate(dp[i]):
                dp[i][j] = dp[i-1][j]
                if j-coins[i-1] >= 0:
                    dp[i][j] += dp[i][j-coins[i-1]]
        return dp[len(coins)][amount]


if __name__ == '__main__':
    print(Solution().change(5, [1,2,5]))