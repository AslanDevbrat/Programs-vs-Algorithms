# Explanation

This algorithm finds the Square Root of an integer (floor value) by using the Binary search algorithm in **O(log(n))** time.

The square root of number n lies between [0,n]
I created a function **find_floor_sqrt( number, start, stop)** where 

 - number: It is the number of which we want to find the square-root.
 - start:  It is the lower limit for the final answer
 - stop: It is the upper limit of the final answer

## **Base Case**

When lower exceeds the upper limit(i.e., start exceeds stop) the function returns the stop value because we want the floor value ( if you wish to get the ceiling value you can change return statement to return start)

The function finds the mid value of start and stop then if the square of the mid is equal to the number the return the mid.


## **Recursion**

If the square of the mid is smaller than the number, then it recurses on 
**find_floor_sqrt( number, mid+1, stop)**

If the square of the mid is greater than the number, then it recurses on 
**find_floor_sqrt( number, 0, mid-1)**

In this every time the interval in which square root is to be find got halved henced the O(log(n))
