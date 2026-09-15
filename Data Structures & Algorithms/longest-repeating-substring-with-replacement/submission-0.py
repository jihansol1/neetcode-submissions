class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        output = 0
        m = {}

        for r in range(0, len(s)):
            # update map count 
            m[s[r]] = 1 + m.get(s[r], 0)
            # if invalid winow
            while (r-l+1) - max(m.values()) > k:
                m[s[l]] -= 1
                l += 1

            # if valid window
            output = max(output, r-l+1)

        return output
