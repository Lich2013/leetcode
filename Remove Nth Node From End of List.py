# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head is None:
            return head
        firstNode = head
        nNode = None
        count = 0
        while firstNode is not None:
            firstNode = firstNode.next
            count += 1
            if count == n+1:
                nNode = head
            if count > n+1:
                nNode = nNode.next
        if nNode is None:
            head = head.next
        else:
            nNode.next = nNode.next.next

        return head

if __name__ == '__main__':
    l = ListNode(1)
    tmp = l
    for i in range(2, 5):
        tmp.next = ListNode(i)
        tmp = tmp.next
    l = Solution().removeNthFromEnd(l, 1)
    while l is not None:
        print(l.val)
        l = l.next