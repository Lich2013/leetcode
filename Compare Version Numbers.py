class Solution(object):
    def compareVersion(self, version1, version2):
        version1 = [int(v) for v in version1.split(".")]
        version2 = [int(v) for v in version2.split(".")]
        for i in range(max(len(version1), len(version2))):
            x = version1[i] if i < len(version1) else 0
            y = version2[i] if i < len(version2) else 0
            if x > y:
                return 1
            elif x < y:
                return -1
        return 0