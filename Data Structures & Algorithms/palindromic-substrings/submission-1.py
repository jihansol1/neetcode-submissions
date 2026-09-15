class Solution:
    def countSubstrings(self, s: str) -> int:

        res = 0
        
        for i in range(len(s)):
            l, r = i, i
            # odd case
            # when l, r are within range and equal each other, expand and increase count
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1

            # even case
            
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1

        return res