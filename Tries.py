#  Implementation of Tries
'''
Tries are used to search for a word in dictionary
it is a tree which contains the dictionary words in a form of a tree representation 
                        a
                        |
                        /\
                    n     ab
                    /\
                t      d
it is used for searching for words 

                
'''

class TrieNode:
    def __init__(self):
        self.children = [None]* 26
        #  [None, None, None, ...]
        self.end = False
#  starting with a simple node 

class Trie:
    def __init__(self):
        '''
        Initialize this data structure
        '''
        self.root = TrieNode()
    
    def insert(self, word:str) -> None:
        curr = self.root
        for c in word:
            i = ord(c) - ord('a')
            if not curr.children[i]:
                curr.children[i] = TrieNode()
                # because we are creating a word out of it so until 
                #  we reach last entry of this word we keep on adding trieNode to the tail
            curr = curr.children[i]
            # move to the child node
        curr.end =  True
    
    def search(self, word:str)-> bool:
        """
        Returns if there is this word in the trie
        """
        curr = self.root
        for c in word:
            i = ord(c) - ord('a')
            if curr.children[i] == None:
                return False
            curr = curr.children[i]

        return curr.end
    
    def startswith(self, word:str) -> bool:
        curr = self.root
        for c in word:
            i = ord(c) - ord("a")
            if curr.children[i] == None:
                return False
            curr = curr.children[i]

        return True
    
def main():
    arr = ["fly", "fair","apple","bat", "edge", "hello", "practice"]
    dic = Trie()
    for i in range(len(arr)):
        dic.insert(arr[i])
    print(dic.search("fly"))
    print(dic.startswith("p"))

if __name__ == "__main__":
    main()
