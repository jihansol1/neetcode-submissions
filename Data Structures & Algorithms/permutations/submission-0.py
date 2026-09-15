class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # base case: if len of nums becomes 0, return empty array
        if len(nums) == 0:
            return [[]]

        # recurse permute function without each first element 
        permutation = self.permute(nums[1:])
        res = []
        for p in permutation:
            for i in range(len(p) + 1):
                p_copy = p.copy()
                p_copy.insert(i, nums[0])
                res.append(p_copy)


        return res

