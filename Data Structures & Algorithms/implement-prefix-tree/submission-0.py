

class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class PrefixTree:

    # initialize the prefix tree object
    def __init__(self):
        self.root = TrieNode()

        
    # insert the string word into the prefix tree
    def insert(self, word: str) -> None:
        curr = self.root
        # go through the word
        for char in word:
            # if the char not in prefix tree -> add 
            if char not in curr.children:
                curr.children[char] = TrieNode()
            # if char in prefix tree, traverse down to its child
            curr = curr.children[char]
        # if word fully inserted, mark end of word
        curr.endOfWord = True

    # return true if the string word is in the prefix tree and false otherwise
    def search(self, word: str) -> bool:
        curr = self.root
        # go through the word
        for char in word:
            # if char not in children, return False
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.endOfWord
        
    # return true if there is a previously interted string word that has the prefix, and false otherwise
    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
            
        return True
        
        