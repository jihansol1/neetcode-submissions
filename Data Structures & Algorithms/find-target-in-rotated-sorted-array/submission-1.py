class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l <= r:
            m = (l+r) // 2
            if nums[m] == target:
                return m

            # if left side is sorted
            if nums[l] <= nums[m]:
                # is target between l and m
                if target >= nums[l] and target <= nums[m]:
                    # yes -> search left side of m
                    r = m - 1
                # no -> search right side of m
                else:
                    l = m + 1
            
            # if right side is sorted
            else:
                # is target between m and r
                if target >= nums[m] and target <= nums[r]:
                    # yes -> search right side of m
                    l = m+1
                # no -> search left side of m
                else:
                    r = m - 1

        return -1
