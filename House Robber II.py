from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums1, nums2 = [nums[0]] if len(nums[:-1]) == 0 else nums[:-1], nums[1:]
        nums1Maximum = 0
        pre = cur = 0
        for num in nums1:
            cur, pre = max(pre+num, cur), cur
        nums1Maximum = cur
        pre = cur = 0
        for num in nums2:
            cur, pre = max(pre+num, cur), cur
        return max(nums1Maximum, cur)


if __name__ == '__main__':
    print(Solution().rob([1]))