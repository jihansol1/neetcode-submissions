class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        s = set(nums)
        count = 0

        for num in s:
            if (num - 1) not in s:
                streak = 1
                while (num + streak) in s:
                    streak += 1
                count = max(count, streak)

        return count

        

