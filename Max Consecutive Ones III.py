from typing import List

class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        count = 0
        past = 0
        longest = 0
        while count < len(A):
            if K > 0:
                if A[count] == 0:
                    K -= 1
                count += 1
            else:
                if A[count] == 1:
                    count += 1
                else:
                    if A[past] == 0:
                        K += 1
                    past += 1
            longest = max(longest, count-past)
        return longest
                
if __name__ == '__main__':
    print(Solution().longestOnes([0,0,1,1,0,1,0,1,0,0,0],3))
            
                    