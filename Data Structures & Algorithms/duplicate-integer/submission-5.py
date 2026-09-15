class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # duplicate = set(nums)

        # if len(duplicate) == len(nums):
        #     return False
        # else: 
        #     return True

        duplicate = set()
        for num in nums:
            if num in duplicate: 
                return True
            duplicate.add(num)

        return False

        