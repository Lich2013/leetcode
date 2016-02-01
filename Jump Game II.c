int jump(int* nums, int numsSize) {
    int step = 0, current_index = 0, last_index = 0;
    for (int i = 0; i < numsSize; i++) {
        if (i > last_index) {
            ++step;
            last_index = current_index;
        }
        if(i + nums[i] > current_index) {
            current_index = i + nums[i];
        }
    }
    return step;
}