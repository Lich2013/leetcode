from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start, end = 0, len(numbers)-1
        while start < end:
            if numbers[start] + numbers[end] == target:
                break
            if numbers[start] + numbers[end] < target:
                start += 1
                continue
            if numbers[start] + numbers[end] > target:
                end -= 1  
        return [start+1, end+1]

if __name__ == '__main__':
    print(Solution().twoSum([-1,0], -1))