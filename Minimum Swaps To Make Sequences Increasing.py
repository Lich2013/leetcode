from typing import List

class Solution:
    def minSwap(self, A: List[int], B: List[int]) -> int:
        n1, s1 = 0, 1
        if len(A) == 1:
            return 0
        for i in range(1, len(A)):
            n2 = s2 = 1000
            if A[i-1] < A[i] and B[i-1] < B[i]:
                n2 = min(n2, n1)
                s2 = min(s2, s1+1)
            if A[i-1] < B[i] and B[i-1] < A[i]:
                n2 = min(n2, s1)
                s2 = min(s2, n1+1)
            s1, n1 = s2, n2
        return min(s1, n1)


        
if __name__ == '__main__':
    print(Solution().minSwap([1, 3, 5, 4], [1, 2, 3, 7]))