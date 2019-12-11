from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        result = []
        tmpStack = [root]
        while tmpStack:
            tmp = tmpStack.pop()
            result.append(tmp.val)
            if tmp.left is not None:
                tmpStack.append(tmp.left)
            if tmp.right is not None:
                tmpStack.append(tmp.right)
        return result[::-1]


if __name__ == '__main__':
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    print(Solution().postorderTraversal(root))