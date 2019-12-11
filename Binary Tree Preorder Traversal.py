from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        result = []
        tmpStack = [root]
        while tmpStack:
            tmp = tmpStack.pop()
            result.append(tmp.val)
            if tmp.right is not None:
                tmpStack.append(tmp.right)
            if tmp.left is not None:
                tmpStack.append(tmp.left)
        return result


if __name__ == '__main__':
    root = TreeNode(3)
    root.right = TreeNode(1)
    root.right.left = TreeNode(2)
    print(Solution().preorderTraversal(root))