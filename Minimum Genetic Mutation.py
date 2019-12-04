from typing import List
from collections import deque


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bfs = deque()
        bfs.append((start, 0))
        step = 0
        bank = set(bank)
        while len(bfs) != 0:
            s, step = bfs.popleft()
            if s == end:
                return step
            for i in range(len(end)):
                for x in 'ACGT':
                    if s[i] == x:
                        continue
                    sNew = s[:i] + x + s[i+1:]
                    if sNew not in bank:
                        continue
                    bfs.append((sNew, step+1))
                    bank.remove(sNew)
        return -1


if __name__ == '__main__':
    print(Solution().minMutation("AACCGGTT", "AACCGGTA", ["AACCGGTA"]))