from typing import List

class Solution:
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        #build count map because letter only 26
        sMap = dict()
        count = 0
        for i, s in enumerate(S):
            if s in sMap:
                sMap[s].append(i)
                continue
            sMap[s] = [i]
        for word in words:
            flag = True
            pos = 0
            for i, s in enumerate(word):
                if s in sMap:
                    isHave = False
                    for k, j in enumerate(sMap[s]):
                        if j >= pos:
                            pos = j+1
                            isHave = True
                            break
                    if not isHave:
                        flag = False
                        break
                else:
                    flag = False
                    break
            if flag:
                count += 1
        return count
        