class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        left, right, count = 0, 0, 0
        for x in S:
            if x == '(':
                left += 1
            if x == ')':
                if left > 0:
                    left -= 1
                else:
                    count += 1
        return count + left


if __name__ == '__main__':
    print(Solution().minAddToMakeValid('(()))(()'))