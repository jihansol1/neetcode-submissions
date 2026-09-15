class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = {}
        count = [[] for i in range(len(nums) + 1)]


        for num in nums:
            m[num] = 1 + m.get(num, 0)

        for key, val in m.items():
            count[val].append(key)

        res = []

        for i in range(len(count) - 1, 0, -1):
            for num in count[i]:
                res.append(num)
                if len(res) == k:
                    return res