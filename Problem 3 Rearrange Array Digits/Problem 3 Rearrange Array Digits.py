#!/usr/bin/env python
# coding: utf-8

# In[2]:


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
    #print('left',left,'right',right)
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


# In[3]:


test_function(test_case)


# In[11]:


# Normal cases
print('Normal Cases:')
print('Test 1:')
list_num = [1, 2, 3, 4, 5]
result = rearrange_digits(input_list=list_num)
if result == [531, 42]:
    print('Pass \n')
else:
    print("Fail \n")

print('Test 2:')
list_num = [4, 6, 2, 5, 9, 8]
result = rearrange_digits(input_list=list_num)

if result == [964,852]:
    print('Pass \n')
else:
    print("Fail \n")

print('Test 3:')
list_num = [1, 2, 3]
result = rearrange_digits(input_list=list_num)

if result == [31, 2]:
    print('Pass \n')
else:
    print("Fail \n")

# Edge cases
print('Edge Cases:')
print('Test 4:')
list_num = [1, 1, 1]
result = rearrange_digits(input_list=list_num)

if result == [11, 1]:
    print('Pass \n')
else:
    print("Fail \n")

print('Test 5:')
list_num = [1]
result = rearrange_digits(input_list=list_num)

if result == [1,0]:
    print('Pass \n')
else:
    print("Fail \n")

print('Test 6:')
list_num = []
result = rearrange_digits(input_list=list_num)

if result == [0,0]:
    print('Pass \n')
else:
    print("Fail \n")


# In[ ]:




