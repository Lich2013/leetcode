from typing import List


class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        a = (points[2][0] - points[0][0], points[2][1] - points[0][1])
        b = (points[1][0] - points[0][0], points[1][1] - points[0][1])
        if a == b or a == (0,0) or b == (0,0):
            return False
        if (a[0] == 0 and b[0] == 0) or (a[1] == 0 and b[1] == 0):
            return False
        if b[0] != 0 and b[1] != 0 and a[0]/b[0] == a[1]/b[1]:
            return False
        return True

if __name__ == '__main__':
    print(Solution().isBoomerang([[1,1],[2,2],[3,3]]))