struct ListNode *detectCycle(struct ListNode *head) {
    struct ListNode *fast = head, *slow = head, *origin = head;
    while (fast != NULL && fast->next != NULL) {
        fast = fast->next->next;
        slow = slow->next;
        if(slow == fast) {
            while(slow != origin) {
                slow = slow->next;
                origin = origin->next;
            }
            return slow;
        }
    }
    return NULL;
}