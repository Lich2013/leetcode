from typing import List
from collections import Counter
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       count = Counter(nums)
       return heapq.nlargest(k, count.keys(), count.get)


if __name__ == '__main__':
    print(Solution().topKFrequent([1,1,1,2,2,3], 2))