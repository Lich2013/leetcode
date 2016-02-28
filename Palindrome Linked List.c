struct ListNode* reverseList(struct ListNode* head) {
    struct ListNode *pre, *cur, *next;
    pre = head;
    cur = head->next;
    while (cur) {
        next = cur->next;
        cur->next = pre;
        pre = cur;
        cur = next;
    }
    head->next = NULL;
    head = pre;
    return head;
}

bool isPalindrome(struct ListNode* head) {
    if(!head || !head->next) {
        return true;
    }
    struct ListNode *fast, *slow;
    fast = head;
    slow = head;
    while(fast && fast->next){
        fast = fast->next->next;
        slow = slow->next;
    }
    if (fast) {
        slow->next = reverseList(slow->next);
        slow = slow->next;
    } else {
        slow = reverseList(slow);
    }
    while (slow) {
        if (head->val != slow->val) {
            return false;
        }
        head = head->next;
        slow = slow->next;
    }
    return true;
}