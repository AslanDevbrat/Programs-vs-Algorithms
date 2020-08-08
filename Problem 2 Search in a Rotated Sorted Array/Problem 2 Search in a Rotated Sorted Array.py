#!/usr/bin/env python
# coding: utf-8

# In[3]:


def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    temp = search_using_recurrsion(input_list,number,0,len(input_list)-1)
    #print('temp',temp)
    return temp

def search_using_recurrsion(arr,target,start,end):
    mid = (start+end)//2
    
    #base case:
    #print('mid',mid)
    if start>end:
        return -1
    
    #if the target at middle element
    if arr[mid] == target:
        return mid
    
    
    # that means arr[start:mid ] is sorted
    if arr[start]<=arr[mid] : 
        
        # if target lies between arr[start:mid]
        if arr[start]<=target<arr[mid]:      
            return search_using_recurrsion(arr,target,start,mid-1)
        return search_using_recurrsion(arr,target,mid+1,end)
    
    
    # that means arr[start:mid ] is not sorted
    elif arr[start]>arr[mid]:    
        if  arr[mid]>target>=arr[end]:
            return search_using_recurrsion(arr,target,mid+1,end)
        return search_using_recurrsion(arr,target,start,mid-1)
    
    
def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    #print(linear_search(input_list, number))
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])


# In[4]:


print('Edge Cases:')
test_function([[], -1])
test_function([[1], 0])


# In[ ]:




