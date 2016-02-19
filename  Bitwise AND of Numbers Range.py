class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        if(m == n):
            return m
        bits = 0
        while m != n:
            m >>= 1
            n >>= 1
            bits += 1
        return m << bits