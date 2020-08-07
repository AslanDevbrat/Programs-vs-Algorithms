#!/usr/bin/env python
# coding: utf-8

# In[41]:


def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    def find_floor_sqrt(number,start,stop):
        #print(start,stop)
        if start>stop:      # Base case: Since we want floor value we returned stop
            return stop
        
        mid = (start+stop)//2
        mid_square = mid**2
        if mid_square == number :
            return mid
        elif mid_square <number:
            return find_floor_sqrt(number,mid+1,stop)
        else:
            #print('grater')
            
            return find_floor_sqrt(number,start,mid-1)
    temp =find_floor_sqrt(number,0,number)
    #print(temp)
    return temp

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")


# In[ ]:




