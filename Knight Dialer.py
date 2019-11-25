class Solution:
    route = {
        0:(4,6),
        1:(6,8),
        2:(7,9),
        3:(4,8),
        4:(0,3,9),
        5:(),
        6:(0,1,7),
        7:(2,6),
        8:(1,3),
        9:(2,4)
    }

    def knightDialer(self, N: int) -> int:
        count = 0
        mod = 10**9+7
        dp = [[0]*10 for _ in range(N)]
        for i in range(10): dp[0][i] = 1

        for i in range(1, N):
            for start in self.route:
                for x in self.route[start]:
                    dp[i][start] += dp[i-1][x]
                dp[i][start] %= mod
        return sum(dp[N-1])%mod

if __name__ == '__main__':
    print(Solution().knightDialer(19))