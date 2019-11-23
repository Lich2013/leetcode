from typing import List

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        return self.dfs(arr, '', 0)


    def dfs(self, arr: List[str], s: str, index: int) -> int:
        if index == len(arr):
            return len(s)
        tmp = s + arr[index]
        if len(set(tmp)) == len(tmp):
            return max(self.dfs(arr, tmp, index+1), self.dfs(arr, s, index+1))
        return self.dfs(arr, s, index+1)



if __name__ == '__main__':
    print(Solution().maxLength(["abcdefghijklm","bcdefghijklmn","cdefghijklmno","defghijklmnop","efghijklmnopq","fghijklmnopqr","ghijklmnopqrs","hijklmnopqrst","ijklmnopqrstu","jklmnopqrstuv","klmnopqrstuvw","lmnopqrstuvwx","mnopqrstuvwxy","nopqrstuvwxyz","opqrstuvwxyza","pqrstuvwxyzab"]))