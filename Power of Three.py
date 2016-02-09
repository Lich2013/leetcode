class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int 3**19 < 2**31 < 3**20
        :rtype: bool
        """
        if n <= 0:
            return False
        if 1162261467 % n == 0:
            return True
        else:
            return False
