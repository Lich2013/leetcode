from typing import List


class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        length = len(A)
        cur = int(length/2-1 if length%2 == 0 else (length-1)/2)
        if A[cur-1] < A[cur] > A[cur+1]:
            return cur
        if  A[cur-1] > A[cur] > A[cur+1]:
            return self.peakIndexInMountainArray(A[:cur+1])
        return cur+self.peakIndexInMountainArray(A[cur:])


if __name__ == '__main__':
    print(Solution().peakIndexInMountainArray([0,1,2,0]))