#!/usr/bin/env python
# coding: utf-8

# In[3]:


def sort_012(arr):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    index_of_0 = 0
    index_of_2 = len(arr)-1
    
    i = 0
    while i<=index_of_2:
        if arr[i] == 0:
            arr[index_of_0] ,arr[i]= 0,arr[index_of_0]
            index_of_0+=1
            i+=1
        elif arr[i] == 2:
            arr[index_of_2],arr[i] =2, arr[index_of_2]
            index_of_2-=1
        else:
            i+=1
    return arr


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
# Edge cases
print('Edge Cases:')
test_function([0, 1, 1, 0, 1])
test_function([0, 0, 0])
test_function([])


# In[ ]:




