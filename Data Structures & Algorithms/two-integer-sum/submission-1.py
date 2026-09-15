class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h_map = {}
        
        for i in range(len(nums)):
            find = target - nums[i]
            if find in h_map:
                return [h_map[find], i]

            h_map[nums[i]] = i
