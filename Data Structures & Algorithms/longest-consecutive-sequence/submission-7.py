class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_set = set()

        for num in nums:
            my_set.add(num)

        ans = 0
        for num in my_set:
            if num-1 not in my_set:
                count = 1
                while num+1 in my_set:
                    count += 1
                    num += 1

                ans = max(ans, count)

        return ans


