#!/usr/bin/env python
# coding: utf-8

# In[5]:


def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    max = -float('inf')
    min = float('inf')
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

# Edge cases
print('Edge Cases:')
# Case 3
l = [i for i in range(300, 301)]  # a list containing 300
random.shuffle(l)
print("Pass" if ((300, 300) == get_min_max(l)) else "Fail")

# Case 4
l = []  # an empty list

print("Pass" if ((float('inf'), -float('inf')) == get_min_max(l)) else "Fail")

# Case 5
l = [i for i in range(-24, -1)]  # a list containing -24 - -2
random.shuffle(l)
print("Pass" if ((-24, -2) == get_min_max(l)) else "Fail")


# In[ ]:





# In[ ]:




