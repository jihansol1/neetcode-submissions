class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        out = 0

        for num in s:
            if num-1 not in s:
                length = 1
                while num + length in s:
                    length += 1
                out = max(length, out)

        return out

        