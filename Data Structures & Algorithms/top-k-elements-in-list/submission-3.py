class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # use bucket sort 
        m = {}
        count = [[] for i in range(len(nums) + 1)]
        for num in nums:
            m[num] = m.get(num, 0) + 1

        for num, freq in m.items():
            count[freq].append(num)

        ans = []
        for i in range(len(count)-1, -1, -1):
            for num in count[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans



            