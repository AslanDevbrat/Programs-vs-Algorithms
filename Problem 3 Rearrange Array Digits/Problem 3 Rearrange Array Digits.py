#!/usr/bin/env python
# coding: utf-8

# In[18]:


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    
    # We are going to use mergeSort to sort the input_list
    # in decending order
    sorted_arr= mergeSort(input_list)
    
    ##Once we got the sorted arr then just traverse the arr
    # and put number in the result[0] and result[1] alternatively
    result = [0,0]
    is_right = False
    for ele in sorted_arr:
        ele = str(ele)
        if is_right:
            result[1] = int(str(result[1]) + ele)
            is_right = False
        else:
            result[0] = int(str(result[0]) + ele)
            is_right = True
    #print(result)
    return result


def mergeSort(items):
    
    if len(items)<=1:
        return items
    
    mid = len(items)//2
    left = items[:mid]
    right = items[mid:]
    
    left = mergeSort(left)
    right = mergeSort(right)
    print('left',left,'right',right)
    temp = merge(left,right)
    #print(temp)
    return temp

def merge(left,right):
    merged = []
    left_index=0
    right_index = 0
        
    while left_index<len(left) and right_index<len(right):
        if left[left_index] >right[right_index]:
            merged.append(left[left_index])
            left_index+=1
        else:
            merged.append(right[right_index])
            right_index+=1
    merged+=left[left_index:]
    merged+=right[right_index:]
    return merged
        

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [531, 42]])
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]


# In[16]:


test_function(test_case)


# In[ ]:




