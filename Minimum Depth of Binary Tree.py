class Solution(object):
    def minDepth(self, root):
        if root is None:
            return 0
        list, depth = [], 0
        list.append(root)
        while(list):
            tmp = []
            depth += 1
            for node in list:
                if (node.right is None and node.left is None):
                    return depth
                if(node.left is not None):
                    tmp.append(node.left)
                if(node.right is not None):
                    tmp.append(node.right)
            list = tmp
        