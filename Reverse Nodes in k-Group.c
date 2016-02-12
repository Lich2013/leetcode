struct ListNode* reverseKGroup(struct ListNode* head, int k) {
    if (k <= 1 || !head) {
        return head;
    }
    struct ListNode *pre, *cur, *next, *result = NULL, *tmp;
    int count = 0;
    tmp = head;
    while (tmp) {
        ++count;
        tmp = tmp->next;
    }
    tmp = NULL;
    count = count/k;
    if (count == 0) {
        return head;
    }
    while (count) {
        --count;
        pre = head;
        cur = head->next;
        for (int i = 0; i < k-1; i++) {
            next = cur->next;
            cur->next = pre;
            pre = cur;
            cur = next;
        }
        head->next = cur;
        if (!tmp) {
            tmp = head;
        } else {
            tmp->next = pre;
            tmp = head;
        }
        head = cur;
        if (!result) {
            result = pre;
        }
    }
    return result;
}