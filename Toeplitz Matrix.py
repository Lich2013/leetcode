from typing import List


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for i, x in enumerate(matrix):
            if i == 0:
                continue
            for j, y in enumerate(x):
                if j == 0:
                    continue
                if matrix[i][j] != matrix[i-1][j-1]:
                    return False
        return True

if __name__ == '__main__':
    matrix = [
  [1,2],
  [2,2]
]
    print(Solution().isToeplitzMatrix(matrix))