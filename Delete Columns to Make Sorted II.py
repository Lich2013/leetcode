from typing import List

class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        count = 0
        if len(A) <= 1:
            return count
        okIndex = ['']*len(A)
        for i in range(len(A[0])):
            isOk = True
            for j in range(1, len(A)):
                if okIndex[j-1] == okIndex[j] and A[j-1][i] > A[j][i]:
                    count += 1
                    isOk = False
                    break
            if isOk:
              for j in range(len(A)):     
                okIndex[j] += A[j][i]    
        return count
