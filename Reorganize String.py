class Solution:
    def reorganizeString(self, S: str) -> str:
        if len(S) == 0:
            return ''
        letterCount = [0]*26
        for x in S:
            letterCount[ord(x)-97] += 1
        if max(letterCount)*2 > len(S)+1:
                return ''
        cur = letterCount.index(max(letterCount))
        letterCount[cur] -= 1
        s = chr(cur+97)
        for _ in range(len(S)-1):
            maxNum = 0
            index = 0
            for i, v in enumerate(letterCount):
                if i == cur:
                    continue
                if maxNum < v:
                    maxNum, index = v, i
            s += chr(index+97)
            cur = index
            letterCount[cur] -= 1
        return s

if __name__ == '__main__':
    print(Solution().reorganizeString("bbrst"))