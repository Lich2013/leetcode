class Solution(object):
    def isValidSerialization(self, preorder):
        list = preorder.split(',')
        count = 1
        for node in list:
            count -= 1
            if(count < 0):
                return False
            if(node != '#'):
                count += 2
        return count == 0
        