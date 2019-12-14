from typing import List


class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        countMap = dict()
        for x in A.split(' '):
            if x in countMap:
                countMap[x] += 1
            else:
                countMap[x] = 1
        for x in B.split(' '):
            if x in countMap:
                countMap[x] += 1
            else:
                countMap[x] = 1
        return [x for x in countMap if countMap[x] == 1]


if __name__ == '__main__':
    print(Solution().uncommonFromSentences("this apple is sweet", "this apple is sour"))