class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate = set(nums)

        if len(duplicate) == len(nums):
            return False
        else: 
            return True
