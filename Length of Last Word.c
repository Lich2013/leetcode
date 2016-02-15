int lengthOfLastWord(char* s) {
    int len = 0, tmp = 0;
    while (*s) {
        (*s == ' ') ? (tmp = 0) : (++tmp);
        tmp != 0 ? (len = tmp): tmp;
        ++s;
    }
    return len;
}