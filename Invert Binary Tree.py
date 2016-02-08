class Solution(object):
    def invertTree(self, root):
        if root is None:
            return None
        list = []
        list.append(root)
        while(list):
            tmp = list.pop()
            tmp.left, tmp.right = tmp.right, tmp.left
            if(tmp.right is not None):
                list.append(tmp.right)
            if(tmp.left is not None):
                list.append(tmp.left)
        return root