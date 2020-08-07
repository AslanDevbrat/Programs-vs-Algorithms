#!/usr/bin/env python
# coding: utf-8

# In[17]:


def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    max = -1
    min = 999999999
    for index,num in enumerate(ints):
        if ints[index]>max:
            max = ints[index]
        if  ints[index]<min:
            min = ints[index]
    
    return(min,max)

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 123)]  # a list containing 0 - 9
random.shuffle(l)
#print(l)
print ("Pass" if ((min(l),max(l)) == get_min_max(l)) else "Fail")

l = [i for i in range(0, 1)]  # a list containing 0 - 9
random.shuffle(l)
#print(l)
print ("Pass" if ((min(l),max(l)) == get_min_max(l)) else "Fail")

l = [i for i in range(0, 999)]  # a list containing 0 - 9
random.shuffle(l)
#print(l)
print ("Pass" if ((min(l),max(l)) == get_min_max(l)) else "Fail")

l = [i for i in range(0, 9)]  # a list containing 0 - 9
random.shuffle(l)
#print(l)
print ("Pass" if ((min(l),max(l)) == get_min_max(l)) else "Fail")


# In[ ]:





# In[ ]:




