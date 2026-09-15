class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // key = number, value = index
        unordered_map<int, int> map;
        
        for (int i=0; i<nums.size(); i++) {
            int found = target - nums[i];
            // if comlement value is found in the map
            if (map.find(found) != map.end()) {
                return {map[found], i};
            }
            // if complement value is not found in the map, add it as new pair
            map[nums[i]] = i;
        }
        // no complement found (no solution)
        return {};
    }
};