# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if root is None:
            return None
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            if root.left is not None and root.right is not None:
                tmp = root.left
                while tmp.right is not None:
                    tmp = tmp.right
                root = self.deleteNode(root, tmp.val)
                root.val = tmp.val
            else:
                root = root.left if root.right is None else root.right
        return root
