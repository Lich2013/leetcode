public class Solution {
    public int majorityElement(int[] nums) {
        int tmp = 0, count = 0;
        for (int i = 0; i < nums.length; i++) {
            if(count == 0) {
                tmp = nums[i];
                ++count;
            } else {
                if (tmp == nums[i]) {
                    ++count;
                } else {
                    --count;
                }
            }
        }
        return tmp;
    }
}