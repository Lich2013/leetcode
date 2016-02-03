struct ListNode* reverseBetween(struct ListNode* head, int m, int n) {
    if(m == n) {
        return head;
    }
    struct ListNode *pre, *cur, *next, *result, *end = NULL;
    result = head;
    for (int i = 1; i < m; i++) {
        end = head;
        head = head->next;
    }
    pre = head;
    cur = head->next;
    for (int i = m; i < n; i++) {
        next = cur->next;
        cur->next = pre;
        pre = cur;
        cur = next;
    }
    head->next = cur;
    if (m == 1) {
        head = pre;
        return head;
    }
    end->next = pre;
    return result;
}