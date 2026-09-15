class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # only uppercase characters and integer k
        # choose up to k characters of the string and replace with any other uppercase english character


        # (r-l+i) - new characters > k then need to adjust the window

        l = 0
        output = 0
        m = {}

        for r in range(len(s)):
            m[s[r]] = m.get(s[r], 0) + 1
            if (r-l+1) - max(m.values()) > k:
                m[s[l]] -= 1
                l += 1
            output = max(output, r-l+1)

        return output
