class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort the nums array
        nums.sort()
        res = []

        for i in range(len(nums)-2):
            # since sorted, duplicates are next to each other so skip when found
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l = i+1
            r = len(nums) - 1

            while l < r:
                sum = nums[l] + nums[r] + nums[i]
                
                if sum == 0:
                    res.append([nums[i],nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # skip duplicates for the pointers
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                elif sum > 0:
                    r -= 1
                else: 
                    l += 1
        return res


        