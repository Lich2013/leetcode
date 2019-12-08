from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        countMap = dict()
        for x in arr:
            if x in countMap:
                countMap[x] += 1
            else:
                countMap[x] = 1
        countList = []
        for x in countMap:
            countList.append(countMap[x])
        return True if len(set(countList)) == len(countList) else False

if __name__ == '__main__':
    print(Solution().uniqueOccurrences([1,2]))