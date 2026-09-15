class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l = 0
        length = 0
        m = {}

        for r in range(len(s)):
            # add mapping of char : frequency
            m[s[r]] = m.get(s[r], 0) + 1
            # if length - max frequency value in map > k, it means need to update window
            if (r-l+1) - max(m.values()) > k:
                m[s[l]] -= 1
                l += 1
            # update length val if necessary
            length = max(length, r-l+1)

        return length
                





