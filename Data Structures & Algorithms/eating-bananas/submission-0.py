class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        i piles of bananas
        h: number of hours you have to eat all bananas
        k: bananas per hour eating rate
        FIND min k such that you can eat all bananas within h hours
        """

        # binary search for the eating speed min k  
        l, r = 1, max(piles)
        ans = float('inf')

        while l <= r:
            m = (l+r) // 2
            hours = 0
            for i in range(len(piles)):
                # get the ceiling for division
                hours += ((piles[i]+m-1) // m)

            # current speed takes too long -> increase min k
            if hours > h:
                l = m+1
            # current speed is less than or equal to h -> update k, try lower k
            elif hours <= h:
                ans = min(ans, m)
                r = m-1
            
        return ans


        