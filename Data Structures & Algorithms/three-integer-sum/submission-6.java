class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        // Sort the array
        Arrays.sort(nums);
        // Count number of occurences in sorted array
        Map<Integer, Integer> count = new HashMap<>();
        for(int num: nums){
            count.put(num, count.getOrDefault(num, 0) + 1);
        }
        

        List<List<Integer>> res = new ArrayList<>();
        for (int i = 0; i < nums.length; i++){
            count.put(nums[i], count.get(nums[i]) - 1);
            if (i > 0 && nums[i] == nums[i - 1]) continue; // skip duplicate

            for (int j = i + 1; j < nums.length; j++){
                count.put(nums[j], count.get(nums[j]) - 1);
                if ( j > i + 1 && nums[j] == nums[j - 1]) continue; // skip duplicate

                int target = -(nums[i] + nums[j]);
                if (count.getOrDefault(target, 0) > 0){ // check if target is in count map
                    res.add(Arrays.asList(nums[i], nums[j], target));
                }
            }
            // Restore count by adding it back
            for (int j = i + 1; j < nums.length; j++){
                count.put(nums[j], count.get(nums[j]) + 1);
            }
        }
        return res;
    }
}
