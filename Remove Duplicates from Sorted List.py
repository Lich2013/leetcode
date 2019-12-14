# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        pre, nxt = head, head.next
        while nxt is not None:
            if nxt.val == pre.val:
                pre.next = nxt = nxt.next
            else:
                pre, nxt = nxt, nxt.next
        return head


if __name__ == '__main__':
    tmp = head = ListNode(1)
    for x in [1,2,3,3]:
    	tmp.next = ListNode(x)
    	tmp = tmp.next
    tmp = head
    while tmp is not None:
    	print(tmp.val)
    	tmp = tmp.next
    print('----')
    tmp = Solution().deleteDuplicates(head)
    while tmp is not None:
    	print(tmp.val)
    	tmp = tmp.next
