class Solution:

    def encode(self, strs: List[str]) -> str:
        # encode a list of strings to a string
        encoded = ""
        for word in strs:
            encoded += str(len(word)) + "#"
            encoded += word
        return encoded


    def decode(self, s: str) -> List[str]:  
        # decode the string back to a list of strings
        # go through the str and seprate words through "(length of string)#"
        output = []
        l = 0
        while l < len(s):
            r = l
            while s[r] != "#":
                r += 1
            length = int(s[l:r])

            word = s[r+1:r+length+1]
            output.append(word)
            
            l = r + length + 1
        
        return output
                




