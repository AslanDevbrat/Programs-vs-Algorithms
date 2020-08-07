#!/usr/bin/env python
# coding: utf-8

# In[120]:


# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self,handler=None):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode()
        self.handler = handler

    def insert(self, url,handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        path_block_list = self.split_path(url)
        current_node=self.root
        for block in path_block_list:
            if block not in current_node.children:
                current_node.insert(block)
            current_node=current_node.children[block]
            #current_node.handler = "not found handler"   
        current_node.handler = handler
            
    def __repr__(self):
        current_node=self.root.children
        while current_node:
            for key in current_node:
                print(current_node)
                current_node = current_node[key].children
        
    def split_path(self, path): 
        #print([ y for y in path.split("/") if y])
        return [ y for y in path.split("/") if y]
    
    def find(self,path):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        current_node = self.root
        path_block_list = self.split_path(path)
        
        for block in path_block_list:
            if block not in current_node.children:
                return None
            current_node = current_node.children[block]
        #print('handler',current_node.handler)
        return current_node.handler
        
    # A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self,):
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.handler = None
        

    def insert(self, path_block):
        # Insert the node as before
        self.children[path_block] = RouteTrieNode()
 


# In[121]:


class Router:
    def __init__(self, handler,non_found_handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.root  = RouteTrie(handler)
        self.add_handler("/",handler)
        self.handler=non_found_handler
    
    def add_handler(self, path,handler ):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        current_node = self.root
        current_node.insert(path,handler)

    def lookup(self,path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        current_node = self.root
        result= current_node.find(path)
        if not result:
            return self.handler
        return result


    def split_path(self,path):
        # you need to split the path into parts for 
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        return [ y for y in path.split("/") if y]


# In[122]:


# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one


# In[ ]:




