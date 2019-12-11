from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        result = []
        tmpStack = [root]
        tmp = root
        while tmpStack:
            while tmp is not None:
                tmpStack.append(tmp)
                tmp = tmp.left
            tmp = tmpStack.pop()
            result.append(tmp.val)
            tmp = tmp.right
        return result[:-1]


if __name__ == '__main__':
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    print(Solution().inorderTraversal(root))