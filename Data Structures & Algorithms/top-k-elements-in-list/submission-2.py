class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        res = {}
        count = [[] for i in range(len(nums) + 1)]

        for num in nums:
            res[num] = res.get(num, 0) + 1

        for num,freq in res.items():
            count[freq].append(num)

        topk = []
        for i in range(len(count)-1, -1, -1):
            for num in count[i]:
                topk.append(num)
                if len(topk) == k:
                    return topk
