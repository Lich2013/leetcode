from typing import List
from collections import deque

class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        martix = [[dict() for _ in range(n)] for _ in range(n)]
        result = [None] * n
        for [x, y] in red_edges:
            martix[x][y]['red'] = False
        for [x, y] in blue_edges:
            martix[x][y]['blue'] = False

        martix[0][0] = {'white':False}
        result[0] = 0
        q = deque()
        q.append([0, 0, 0, 'red'])
        q.append([0, 0, 0, 'blue'])
        while len(q) > 0:
            [i, j, length, color] = q.popleft()
            needColor = 'red' if color != 'red' else 'blue'
            for x in range(n):
                if len(martix[j][x]) > 0 and needColor in martix[j][x]:
                    if martix[j][x][needColor] is False:
                        martix[j][x][needColor] = True
                        q.append([j, x, length+1, needColor])
                        if result[x] is None or result[x] > length+1:
                            result[x] = length+1
        return [x if x is not None else -1 for x in result]

if __name__ == '__main__':
    print(Solution().shortestAlternatingPaths(5, [[0,1],[2,3]], [[1,2],[3,4],[1,4]]))
    print(Solution().shortestAlternatingPaths(5,
        [[0,1],[1,2],[2,3],[3,4]],
        [[1,2],[2,3],[3,1]]))