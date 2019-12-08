class Solution:
    def frequencySort(self, s: str) -> str:
        countMap = dict()
        for x in s:
            if x in countMap:
                countMap[x] += 1
            else:
                countMap[x] = 1
        reverseCountMap = dict()
        countList = []
        for x in countMap:
            countList.append(countMap[x])
            if countMap[x] in reverseCountMap:
                reverseCountMap[countMap[x]].append(x)
            else:
                reverseCountMap[countMap[x]] = [x]
        result = ''
        countList = list(set(countList))
        countList.sort()
        countList.reverse()
        for x in countList:
            for y in reverseCountMap[x]:
                result += y*x
        return result

        
if __name__ == '__main__':
    print(Solution().frequencySort('Aabb'))