class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # Anagrams must have same amount of chars
        if len(s) != len(t):
            return False

        m_s = {}
        for char in s:
            if char in m_s:
                m_s[char] += 1
            else:
                m_s[char] = 0

        m_t = {}
        for char in t:
            if char in m_t:
                m_t[char] += 1
            else:
                m_t[char] = 0

        for c in m_s:
            if c not in m_t or m_s[c] != m_t[c]:
                return False

        return True

        
        