class Solution(object):
    def mySqrt(self, x):
        y = x
        while y*y > x:
            y = (y + x/y)/2
            print y
        return y