class TrieNode:
    def __init__(self):
        self.children={}
        self.is_end_of_the_word=False
class Trie:
    def __init__(self):
        self.root=TrieNode()

    def insert(self,word):
        current=self.root
        for char in word:
            if char not in current.children:
                current.children[char]=TrieNode()
            current=current.children[char]
        current.is_end_of_the_word=True
    
    def search(self,word):
        current=self.root
        for char in word:
            if char not in word:
                return False
            current=current.children[char]
        return current.is_end_of_the_word
    
    def prefix_search(self,word):
        current=self.root
        for char in word:
            if char not in current.children:
                return False
            current=current.children[char]
        return True

    def display(self,node=None,word="",lvl=0):
        if node is None:
            node=self.root
        if node.is_end_of_the_word:
            print("\t"*lvl+word)
        for char,child_node in node.children.items():
            self.display(child_node,word+char,lvl+1)
    

trie=Trie()
with open("C:/Users/jomon/python/python_lab/PYTHON/valid_words.txt","r") as file1:
    for line in file1:
        word=line.strip().lower()
        if word:
            trie.insert(word)
trie.display()
sh="apple"
if trie.search(sh):
    print(sh+"found")
else:
    print(sh+" not found")
