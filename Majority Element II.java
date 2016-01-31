public class Solution {
    public List<Integer> majorityElement(int[] nums) {
        List<Integer> result = new ArrayList<Integer>();
        int tmp0 = new Integer(10), tmp1 = new Integer(10), count0 = 0, count1 = 0;
        for(int i = 0; i < nums.length; i++) {
            if (tmp0 == nums[i]) {
                ++count0;
            } else if (tmp1 == nums[i]) {
                ++count1;
            } else if (count0 == 0) {
                tmp0 = nums[i];
                ++count0;
            } else if (count1 == 0 && tmp0 != nums[i]) {
                tmp1 = nums[i];
                ++count1;
            }else {
                --count0;
                --count1;
            }
        }
        count0 = 0;
        count1 = 0;
        for(int i = 0; i < nums.length; i++) {
            if (tmp0 == nums[i]) {
                ++count0;
            } else if (tmp1 == nums[i]) {
                ++count1;
            }
        }
        if (count0 > nums.length/3) {
            result.add(tmp0);
        }
        if (count1 > nums.length/3) {
            result.add(tmp1);
        }
        return result;
    }
}