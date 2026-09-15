class Solution:

    def encode(self, strs: List[str]) -> str:
        # Given a list of strings, encode it into a single string
        encode_string = ""
        for s in strs:
            encode_string += str(len(s)) + "#" + s
        return encode_string

    5#Hello5#World


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j

        return res
