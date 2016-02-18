class Solution(object):
    def levelOrder(self, root):
        if root is None:
            return []
        result = [[root.val]]
        last_stack = [root]
        new_stack = [root]
        while(new_stack):
            new_stack = []
            result.append([])
            for node in last_stack:
                if node.left is not None:
                    new_stack.append(node.left)
                    result[-1].append(node.left.val)
                if node.right is not None:
                    new_stack.append(node.right)
                    result[-1].append(node.right.val)
            last_stack = new_stack
        return result[:-1]