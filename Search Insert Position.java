public class Solution {
    public int searchInsert(int[] nums, int target) {
        if (target <= nums[0]) {
            return 0;
        }
        int j = nums.length-1;
        int i = 0;
        int tmp = 0;
        while (i <= j) {
            tmp = (i+j)/2;
            if ( target == nums[tmp] || (target < nums[tmp] && target > nums[tmp-1]) ){
                return tmp;
            } else if (target < nums[tmp]) {
                j = tmp-1;
            } else {
                i = tmp+1;
            }
        }
        return i;
    }
}