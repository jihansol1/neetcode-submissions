class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        # create a map with char : freq for s1

        # sliding window for s2
        # if we find the substring according to map in s1 in s2, then we return true
        # if not, always search within the window size of len(s1)

        if len(s1) > len(s2):
            return False 

        s1c, s2c = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1c[ord(s1[i]) - ord('a')] += 1
            s2c[ord(s2[i]) - ord('a')] += 1

        matches = 0

        for i in range(26): 
            if s1c[i] == s2c[i]:
                matches += 1

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            index = ord(s2[r]) - ord('a')
            s2c[index] += 1
            if s1c[index] == s2c[index]:
                matches += 1
            elif s1c[index] + 1 == s2c[index]:
                matches -= 1
            
            index = ord(s2[l]) - ord('a')
            s2c[index] -= 1
            if s1c[index] == s2c[index]:
                matches += 1
            elif s1c[index] - 1 == s2c[index]:
                matches -= 1
            l += 1
        return matches == 26

            

            

        
                



        