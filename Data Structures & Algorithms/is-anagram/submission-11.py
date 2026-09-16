class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # true if s and t are anagrams of each other
        # get hashmap for s and t, compare hashmap 
        if len(s) != len(t):
            return False

        s_map = {}
        t_map = {}

        for i in range(len(s)):
            s_map[s[i]] = s_map.get(s[i], 0) + 1
            t_map[t[i]] = t_map.get(t[i], 0) + 1

        return s_map == t_map

        # time: O(n), space: O(1)
