class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        consecutive = 0
        for num in num_set:
            if num-1 not in num_set:
                streak = num
                count = 1
                while streak+1 in num_set:
                    count += 1
                    streak += 1

                consecutive = max(consecutive, count)
        return consecutive
                
