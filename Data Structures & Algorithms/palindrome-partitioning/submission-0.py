class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        partition = []

        def isPalindrome(word, i, j):
            while i < j:
                if word[i] != word[j]:
                    return False
                i += 1
                j -= 1

            return True

        def dfs(i):
            if i >= len(s):
                res.append(partition.copy())
                return
            
            for j in range(i, len(s)):
                if isPalindrome(s, i, j):
                    partition.append(s[i:j+1])
                    dfs(j+1)
                    partition.pop()

        dfs(0)

        return res