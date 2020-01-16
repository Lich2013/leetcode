class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k >= len(num):
            return '0'
        numStack = []
        for x in num:
            while k > 0 and numStack != [] and x < numStack[-1]:
                numStack.pop()
                k -= 1
            numStack.append(x)
        numStack = numStack[:-k] if k != 0 else numStack
        return ''.join(numStack).lstrip('0') or '0'

if __name__ == '__main__':
    print(Solution().removeKdigits('10', 2))