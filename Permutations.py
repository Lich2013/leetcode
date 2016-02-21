class Solution(object):
    def permute(self, nums):
        result = [[]]
        for x in nums:
            tmp = []
            for perm in result:
                for i in range(len(perm)+1):
                    tmp.append(perm[:i] + [x] + perm[i:])
            result = tmp
        return result