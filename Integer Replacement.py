class Solution:
    def integerReplacement(self, n: int) -> int:
        count = 0
        while n > 3:
            count += 1
            if n & 1 == 0:
                n >>= 1
            elif n & 2 == 0:
                n -= 1
            else: # n & 3 == 3:
                n += 1

        return count+n-1

if __name__ == '__main__':
    print(Solution().integerReplacement(8))