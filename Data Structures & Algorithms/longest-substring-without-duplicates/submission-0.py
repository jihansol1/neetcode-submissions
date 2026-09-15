class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        output = 0
        l = 0
        char_set = set()

        for i in range(len(s)):
            while s[i] in char_set:
                char_set.remove(s[l])
                l += 1
            char_set.add(s[i])
            output = max(output, i-l+1)

        return output


