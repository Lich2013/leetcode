from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        if len(pre) == 0:
            return None
        root = TreeNode(pre[0])
        if len(pre) <= 1:
            return root
        index = post.index(pre[1])+1
        root.left = self.constructFromPrePost(pre[1:index+1], post[:index+1])
        root.right = self.constructFromPrePost(pre[index+1:], post[index:-1])
        return root


if __name__ == '__main__':
    root = Solution().constructFromPrePost([1,2,4,5,3,6,7], [4,5,2,6,7,3,1])
    