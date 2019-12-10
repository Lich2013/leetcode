class Solution:
    def checkValidString(self, s: str) -> bool:
        left, right, star = 0, 0, 0
        for x in s:
            if x == '(':
                left += 1
            elif x == '*':
                star += 1
            else:
                if left > 0:
                    left -= 1
                elif star > 0:
                    star -= 1
                else:
                    return False
        if left > star:
            return False
        left, right, star = 0, 0, 0
        for x in s[::-1]:
            if x == ')':
                left += 1
            elif x == '*':
                star += 1
            else:
                if left > 0:
                    left -= 1
                elif star > 0:
                    star -= 1
                else:
                    return False
        if left > star:
            return False
        return True

if __name__ == '__main__':
    print(Solution().checkValidString("(()()*(()))"))