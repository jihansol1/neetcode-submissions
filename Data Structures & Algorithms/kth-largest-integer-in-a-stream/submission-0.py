class KthLargest:

    # initializes the objhect given integer k, and stream nums
    # intialize a heap
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)

        while len(self.nums) > self.k:
            heapq.heappop(self.nums)

        
    # add an ingeter val to the stream and return the kth largest integer in the stream
    def add(self, val: int) -> int:
        
        # add val, heapify, only keep k items, return last item
        heapq.heappush(self.nums, val)

        if len(self.nums) > self.k:
            heapq.heappop(self.nums)

        
        return self.nums[0]


