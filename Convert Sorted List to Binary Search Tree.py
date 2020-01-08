# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if head is None:
            return None
        pre, slow, fast = None, head, head
        while fast.next and fast.next.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        root = TreeNode(slow.val)
        if pre is not None:
            pre.next = None
            root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(slow.next)
        return root

if __name__ == '__main__':
    Solution()