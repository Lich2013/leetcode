class Solution(object):
    def hasPathSum(self, root, sum):
        if root is None:
            return False
        list = [root]
        list_next = []
        leaf = []
        while(list != []):
            for node in list:
                if node.left == None and node.right == None:
                    leaf.append(node)
                    continue
                if node.left != None:
                    node.left.val += node.val
                    list_next.append(node.left)
                if node.right != None:
                    node.right.val += node.val
                    list_next.append(node.right)
            if list_next == []:
                break
            else:
                list = list_next
                list_next = []
        for node in leaf:
            if node.val == sum:
                return True
        return False