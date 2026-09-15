class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in m:
                return [m[complement], i]
            m[nums[i]] = i

        return []
