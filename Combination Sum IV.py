from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        if len(nums) == 0 or target < 0:
            return 0
        dp = [0 for _ in range(target+1)]
        dp[0] = 1
        for i in range(1, target+1):
            for num in nums:
                if i >= num:
                    dp[i] += dp[i-num]
        return dp[-1]


if __name__ == '__main__':
    print(Solution().combinationSum4([1, 2, 3], -1))