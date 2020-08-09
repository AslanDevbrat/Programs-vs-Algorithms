#!/usr/bin/env python
# coding: utf-8

# # Building a Trie in Python
# 
# Before we start let us reiterate the key components of a Trie or Prefix Tree. A trie is a tree-like data structure that stores a dynamic set of strings. Tries are commonly used to facilitate operations like predictive text or autocomplete features on mobile phones or web search.
# 
# Before we move into the autocomplete function we need to create a working trie for storing strings.  We will create two classes:
# * A `Trie` class that contains the root node (empty string)
# * A `TrieNode` class that exposes the general functionality of the Trie, like inserting a word or finding the node which represents a prefix.
# 
# Give it a try by implementing the `TrieNode` and `Trie` classes below!

# # Finding Suffixes
# 
# Now that we have a functioning Trie, we need to add the ability to list suffixes to implement our autocomplete feature.  To do that, we need to implement a new function on the `TrieNode` object that will return all complete word suffixes that exist below it in the trie.  For example, if our Trie contains the words `["fun", "function", "factory"]` and we ask for suffixes from the `f` node, we would expect to receive `["un", "unction", "actory"]` back from `node.suffixes()`.
# 
# Using the code you wrote for the `TrieNode` above, try to add the suffixes function below. (Hint: recurse down the trie, collecting suffixes as you go.)

# In[1]:


## Represents a single node in the Trie

class TrieNode:

    def __init__(self):
        ## Initialize this node in the Trie
        self.children ={}
        self.is_word = False

    
    def insert(self, char):
        ## Add a child node in this Trie
        self.children[char] = TrieNode()
 
    def suffixes(self, suffix = '',lis=[]):
        ## Recursive function that collects the suffix for 
        ## all complete words below this point
        result = []
        node = self
        for s in suffix:
            if s in node.children:
                node = node.children[s]
            else:
                return result
        self.find_letters(node, suffix, result)
        return result
        
    def find_letters(self, node, letters, result):
        """
        create a list to store words
        for every item in children (letter => node)
        base case => if node is a leaf append word to list of words
        else => list of words += recursive call to collect letters in
        suffix as suffix += letter
        return list of words
        """
        for key, next_node in node.children.items():
            if next_node.is_word:
                result.append(letters+key)
            self.find_letters(next_node, letters+key, result)
            

                
        
## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        temp = self.root
        for char in word:
            if char not in temp.children:
                temp.insert(char)
            temp = temp.children[char]
        temp.is_word = True

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        #print(prefix)
        temp = self.root
        for char in prefix:
            if temp.children.get(char) is None:
                return False
            temp = temp.children[char]
            #print(temp.children)
            
        return temp
    


# # Testing it all out
# 
# Run the following code to add some words to your trie and then use the interactive search box to see what your code returns.

# In[2]:


MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)


# In[3]:


from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact
def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
            
        else:
            print(prefix + " not found")
    else:
        print('')
interact(f,prefix='');


# In[21]:


#Test1
print('Pass' if MyTrie.find('a').suffixes() == ['nt', 'nthology', 'ntagonist', 'ntonym'] else 'Fail')


# In[22]:


#Test2
#EDGE CASE
print('Pass' if MyTrie.find('').suffixes() == ['ant',
 'anthology',
 'antagonist',
 'antonym',
 'fun',
 'function',
 'factory',
 'trie',
 'trigger',
 'trigonometry',
 'tripod'] else 'Fail')


# In[23]:


# Test 3
# EDGE 
print('Pass' if MyTrie.find('as')== False else 'Fail')


# In[ ]:




