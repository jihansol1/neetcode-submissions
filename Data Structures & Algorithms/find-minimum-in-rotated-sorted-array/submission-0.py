class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l, r = 0, len(nums) - 1

        while l < r:
            # check if pivot: if leftmost is less than rightmost, leftmost is min
            if nums[l] < nums[r]:
                return nums[l]
            m = (l+r) // 2
            # if mid val greater than rightmost val -> pivot is on right of mid
            if nums[m] > nums[r]:
                l = m+1
            # if mid val is less than rightmost val -> m can be pivot or pivot on leftside
            elif nums[m] < nums[r]:
                r = m

        return nums[l]
            
            
 
