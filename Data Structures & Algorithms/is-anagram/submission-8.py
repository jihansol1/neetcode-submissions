class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        s_map = {}
        t_map = {}

        for c in s:
            s_map[c] = s_map.get(c, 0) + 1

        for c in t:
            t_map[c] = t_map.get(c, 0) + 1
        
        for char in s_map:
            if s_map[char] != t_map.get(char, 0):
                return False
            
        return True
        