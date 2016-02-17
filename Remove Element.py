class Solution(object):
    def removeElement(self, nums, val):
        for x in nums[:]:
            if x == val:
                nums.remove(val)
        return len(nums)