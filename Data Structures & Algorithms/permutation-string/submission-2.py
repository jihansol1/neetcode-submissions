class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False

        # map char : frequency of s1
        m1 = {}
        for char in s1:
            m1[char] = m1.get(char, 0) + 1

        m2 = {}
        l = 0
        # go through s2 and keep a s2 map frequency
        for r in range(len(s2)):
            m2[s2[r]] = m2.get(s2[r], 0 ) + 1
            # if window is larger than size of s1, reduce window and update map 
            if r-l+1 > len(s1):
                m2[s2[l]] -= 1
                # if frequency = 0, remove the key from map
                if m2[s2[l]] == 0:
                    del m2[s2[l]]
                l += 1 
            # if window == size of s1, compare maps 
            if r-l+1 == len(s1):
                if m1 == m2:
                    return True

        return False

