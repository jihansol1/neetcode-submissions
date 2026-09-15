
class Node:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = Node()
        
    # add word to the trie 
    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = Node()
            curr = curr.children[char]

        curr.endOfWord = True

    
    # return true if there is any string in the trie that matches word, otherwise false.
    # if '.', can be matched with any letter -> use dfs to try every child
    def search(self, word: str) -> bool:

        def dfs(startIndex, root):
            curr = root

            for i in range(startIndex,len(word)):
                char = word[i]
                # if char is ".", need to use recursion
                if char == ".":
                    for child in curr.children.values():
                        if dfs(i+1, child):
                            return True
                    return False

                else:
                    # if word does not exist
                    if char not in curr.children:
                        return False
                    # word exists
                    curr = curr.children[char]

            return curr.endOfWord

        return dfs(0, self.root)


        
